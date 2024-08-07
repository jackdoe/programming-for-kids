#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#ifdef _WIN32
  #include <windows.h>
  #include <winhttp.h>
#else
  #include <curl/curl.h>
#endif
#define MAX_RESPONSE_SIZE 100000
void* allocx(size_t size) {
    void* ptr = allocx(size);
    if (!ptr) {
        fprintf(stderr, "Memory allocation failed\n");
        exit(EXIT_FAILURE);
    }
    return ptr;
}

// Custom reallocation function that exits on failure
void* reallocx(void* ptr, size_t size) {
    void* new_ptr = realloc(ptr, size);
    if (!new_ptr) {
        fprintf(stderr, "Memory reallocation failed\n");
        exit(EXIT_FAILURE);
    }
    return new_ptr;
}

typedef enum {
    JSON_NULL,
    JSON_BOOLEAN,
    JSON_NUMBER,
    JSON_STRING,
    JSON_ARRAY,
    JSON_OBJECT
} JsonType;

typedef struct JsonValue {
    JsonType type;
    union {
        int boolean;
        double number;
        char* string;
        struct {
            struct JsonValue** values;
            int count;
        } array;
        struct {
            char** keys;
            struct JsonValue** values;
            int count;
        } object;
    } value;
} JsonValue;

void skip_whitespace(const char** json) {
    while (isspace(**json)) (*json)++;
}

JsonValue* parse_value(const char** json);

char* parse_string(const char** json) {
    if (**json != '"') return NULL;
    (*json)++;
    
    const char* start = *json;
    while (**json && **json != '"') {
        if (**json == '\\' && *(*json + 1)) (*json)++;
        (*json)++;
    }
    
    if (**json != '"') return NULL;
    
    size_t length = *json - start;
    char* result = allocx(length + 1);
    strncpy(result, start, length);
    result[length] = '\0';
    
    (*json)++;
    return result;
}

JsonValue* parse_object(const char** json) {
    if (**json != '{') return NULL;
    (*json)++;
    
    JsonValue* object = allocx(sizeof(JsonValue));
    object->type = JSON_OBJECT;
    object->value.object.keys = NULL;
    object->value.object.values = NULL;
    object->value.object.count = 0;
    
    skip_whitespace(json);
    
    while (**json && **json != '}') {
        char* key = parse_string(json);
        if (!key) {
            // Handle error
            return object;
        }
        
        skip_whitespace(json);
        
        if (**json != ':') {
            // Handle error
            free(key);
            return object;
        }
        (*json)++;
        
        skip_whitespace(json);
        
        JsonValue* value = parse_value(json);
        if (!value) {
            // Handle error
            free(key);
            return object;
        }
        
        object->value.object.count++;
        object->value.object.keys = reallocx(object->value.object.keys, object->value.object.count * sizeof(char*));
        object->value.object.values = reallocx(object->value.object.values, object->value.object.count * sizeof(JsonValue*));
        
        object->value.object.keys[object->value.object.count - 1] = key;
        object->value.object.values[object->value.object.count - 1] = value;
        
        skip_whitespace(json);
        
        if (**json == ',') {
            (*json)++;
            skip_whitespace(json);
        } else if (**json != '}') {
            // Handle error
            return object;
        }
    }
    
    if (**json == '}') (*json)++;
    return object;
}

JsonValue* parse_array(const char** json) {
    if (**json != '[') return NULL;
    (*json)++;
    
    JsonValue* array = allocx(sizeof(JsonValue));
    array->type = JSON_ARRAY;
    array->value.array.values = NULL;
    array->value.array.count = 0;
    
    skip_whitespace(json);
    
    while (**json && **json != ']') {
        JsonValue* value = parse_value(json);
        if (!value) {
            // Handle error
            return array;
        }
        
        array->value.array.count++;
        array->value.array.values = reallocx(array->value.array.values, array->value.array.count * sizeof(JsonValue*));
        array->value.array.values[array->value.array.count - 1] = value;
        
        skip_whitespace(json);
        
        if (**json == ',') {
            (*json)++;
            skip_whitespace(json);
        } else if (**json != ']') {
            // Handle error
            return array;
        }
    }
    
    if (**json == ']') (*json)++;
    return array;
}

JsonValue* parse_value(const char** json) {
    skip_whitespace(json);
    
    JsonValue* value = allocx(sizeof(JsonValue));
    
    if (**json == '{') {
        free(value);
        return parse_object(json);
    } else if (**json == '[') {
        free(value);
        return parse_array(json);
    } else if (**json == '"') {
        value->type = JSON_STRING;
        value->value.string = parse_string(json);
    } else if (isdigit(**json) || **json == '-') {
        value->type = JSON_NUMBER;
        value->value.number = strtod(*json, (char**)json);
    } else if (strncmp(*json, "true", 4) == 0) {
        value->type = JSON_BOOLEAN;
        value->value.boolean = 1;
        *json += 4;
    } else if (strncmp(*json, "false", 5) == 0) {
        value->type = JSON_BOOLEAN;
        value->value.boolean = 0;
        *json += 5;
    } else if (strncmp(*json, "null", 4) == 0) {
        value->type = JSON_NULL;
        *json += 4;
    } else {
        free(value);
        return NULL;
    }
    
    return value;
}

JsonValue* parse_json(const char* json) {
    return parse_value(&json);
}

char* find_content(JsonValue* json) {
    if (json->type != JSON_OBJECT) return NULL;
    
    for (int i = 0; i < json->value.object.count; i++) {
        if (strcmp(json->value.object.keys[i], "choices") == 0) {
            JsonValue* choices = json->value.object.values[i];
            if (choices->type != JSON_ARRAY || choices->value.array.count == 0) return NULL;
            
            JsonValue* first_choice = choices->value.array.values[0];
            if (first_choice->type != JSON_OBJECT) return NULL;
            
            for (int j = 0; j < first_choice->value.object.count; j++) {
                if (strcmp(first_choice->value.object.keys[j], "message") == 0) {
                    JsonValue* message = first_choice->value.object.values[j];
                    if (message->type != JSON_OBJECT) return NULL;
                    
                    for (int k = 0; k < message->value.object.count; k++) {
                        if (strcmp(message->value.object.keys[k], "content") == 0) {
                            JsonValue* content = message->value.object.values[k];
                            if (content->type != JSON_STRING) return NULL;
                            return strdup(content->value.string);
                        }
                    }
                }
            }
        }
    }
    
    return NULL;
}

void free_json(JsonValue* json) {
    if (!json) return;
    
    switch (json->type) {
        case JSON_STRING:
            free(json->value.string);
            break;
        case JSON_ARRAY:
            for (int i = 0; i < json->value.array.count; i++) {
                free_json(json->value.array.values[i]);
            }
            free(json->value.array.values);
            break;
        case JSON_OBJECT:
            for (int i = 0; i < json->value.object.count; i++) {
                free(json->value.object.keys[i]);
                free_json(json->value.object.values[i]);
            }
            free(json->value.object.keys);
            free(json->value.object.values);
            break;
        default:
            break;
    }
    
    free(json);
}

JsonValue* create_string(const char* str) {
    JsonValue* value = allocx(sizeof(JsonValue));
    value->type = JSON_STRING;
    value->value.string = strdup(str);
    return value;
}

JsonValue* create_object() {
    JsonValue* value = allocx(sizeof(JsonValue));
    value->type = JSON_OBJECT;
    value->value.object.keys = NULL;
    value->value.object.values = NULL;
    value->value.object.count = 0;
    return value;
}

JsonValue* create_array() {
    JsonValue* value = allocx(sizeof(JsonValue));
    value->type = JSON_ARRAY;
    value->value.array.values = NULL;
    value->value.array.count = 0;
    return value;
}

void add_to_object(JsonValue* object, const char* key, JsonValue* value) {
    if (object->type != JSON_OBJECT) return;
    
    object->value.object.count++;
    object->value.object.keys = reallocx(object->value.object.keys, object->value.object.count * sizeof(char*));
    object->value.object.values = reallocx(object->value.object.values, object->value.object.count * sizeof(JsonValue*));
    
    object->value.object.keys[object->value.object.count - 1] = strdup(key);
    object->value.object.values[object->value.object.count - 1] = value;
}

void add_to_array(JsonValue* array, JsonValue* value) {
    if (array->type != JSON_ARRAY) return;
    
    array->value.array.count++;
    array->value.array.values = reallocx(array->value.array.values, array->value.array.count * sizeof(JsonValue*));
    array->value.array.values[array->value.array.count - 1] = value;
}

char* serialize_json(JsonValue* json) {
    char* result = NULL;
    size_t size = 0;
    FILE* stream = open_memstream(&result, &size);
    
    switch (json->type) {
        case JSON_NULL:
            fprintf(stream, "null");
            break;
        case JSON_BOOLEAN:
            fprintf(stream, json->value.boolean ? "true" : "false");
            break;
        case JSON_NUMBER:
            fprintf(stream, "%g", json->value.number);
            break;
        case JSON_STRING:
            fprintf(stream, "\"%s\"", json->value.string);
            break;
        case JSON_ARRAY:
            fprintf(stream, "[");
            for (int i = 0; i < json->value.array.count; i++) {
                if (i > 0) fprintf(stream, ",");
                char* element = serialize_json(json->value.array.values[i]);
                fprintf(stream, "%s", element);
                free(element);
            }
            fprintf(stream, "]");
            break;
        case JSON_OBJECT:
            fprintf(stream, "{");
            for (int i = 0; i < json->value.object.count; i++) {
                if (i > 0) fprintf(stream, ",");
                fprintf(stream, "\"%s\":", json->value.object.keys[i]);
                char* value = serialize_json(json->value.object.values[i]);
                fprintf(stream, "%s", value);
                free(value);
            }
            fprintf(stream, "}");
            break;
    }
    
    fclose(stream);
    return result;
}


#ifdef _WIN32
// Windows implementation
char* chatgpt_windows(const char* prompt, char* api_key) {
    HINTERNET hSession = NULL, hConnect = NULL, hRequest = NULL;
    BOOL bResults = FALSE;
    DWORD dwSize = 0;
    DWORD dwDownloaded = 0;
    LPSTR pszOutBuffer = NULL;
    DWORD dwBufferSize = 0;
    char* result = NULL;
    char* post_fields = NULL;
    JsonValue* request = NULL;
    JsonValue* json_response = NULL;

    // Create JSON object for the request
    request = create_object();
    if (!request) {
        fprintf(stderr, "Memory allocation failed\n");
        goto cleanup;
    }

    add_to_object(request, "model", create_string("gpt-4o-mini"));
    
    JsonValue* messages = create_array();
    if (!messages) {
        fprintf(stderr, "Memory allocation failed\n");
        goto cleanup;
    }

    JsonValue* message = create_object();
    if (!message) {
        fprintf(stderr, "Memory allocation failed\n");
        goto cleanup;
    }

    add_to_object(message, "role", create_string("user"));
    add_to_object(message, "content", create_string(prompt));
    add_to_array(messages, message);
    add_to_object(request, "messages", messages);

    post_fields = serialize_json(request);
    if (!post_fields) {
        fprintf(stderr, "JSON serialization failed\n");
        goto cleanup;
    }

    // Initialize WinHTTP
    hSession = WinHttpOpen(L"ChatGPT API Client", WINHTTP_ACCESS_TYPE_DEFAULT_PROXY, WINHTTP_NO_PROXY_NAME, WINHTTP_NO_PROXY_BYPASS, 0);
    if (!hSession) {
        fprintf(stderr, "WinHttpOpen failed\n");
        goto cleanup;
    }

    // Connect to the server
    hConnect = WinHttpConnect(hSession, L"api.openai.com", INTERNET_DEFAULT_HTTPS_PORT, 0);
    if (!hConnect) {
        fprintf(stderr, "WinHttpConnect failed\n");
        goto cleanup;
    }

    // Create an HTTP request
    hRequest = WinHttpOpenRequest(hConnect, L"POST", L"/v1/chat/completions", NULL, WINHTTP_NO_REFERER, WINHTTP_DEFAULT_ACCEPT_TYPES, WINHTTP_FLAG_SECURE);
    if (!hRequest) {
        fprintf(stderr, "WinHttpOpenRequest failed\n");
        goto cleanup;
    }

    // Add headers
    WCHAR headers[256];
    swprintf(headers, 256, L"Authorization: Bearer %hs\r\nContent-Type: application/json", api_key);
    bResults = WinHttpAddRequestHeaders(hRequest, headers, -1L, WINHTTP_ADDREQ_FLAG_ADD);
    if (!bResults) {
        fprintf(stderr, "WinHttpAddRequestHeaders failed\n");
        goto cleanup;
    }

    // Send the request
    bResults = WinHttpSendRequest(hRequest, WINHTTP_NO_ADDITIONAL_HEADERS, 0, post_fields, strlen(post_fields), strlen(post_fields), 0);
    if (!bResults) {
        fprintf(stderr, "WinHttpSendRequest failed\n");
        goto cleanup;
    }

    // Receive the response
    bResults = WinHttpReceiveResponse(hRequest, NULL);
    if (!bResults) {
        fprintf(stderr, "WinHttpReceiveResponse failed\n");
        goto cleanup;
    }

    // Read the response data
    do {
        dwSize = 0;
        if (!WinHttpQueryDataAvailable(hRequest, &dwSize)) {
            fprintf(stderr, "WinHttpQueryDataAvailable failed\n");
            goto cleanup;
        }

        if (dwSize == 0) {
            break;
        }

        pszOutBuffer = (LPSTR)realloc(pszOutBuffer, dwBufferSize + dwSize + 1);
        if (!pszOutBuffer) {
            fprintf(stderr, "Memory allocation failed\n");
            goto cleanup;
        }

        ZeroMemory(pszOutBuffer + dwBufferSize, dwSize + 1);

        if (!WinHttpReadData(hRequest, (LPVOID)(pszOutBuffer + dwBufferSize), dwSize, &dwDownloaded)) {
            fprintf(stderr, "WinHttpReadData failed\n");
            goto cleanup;
        }

        dwBufferSize += dwDownloaded;

    } while (dwSize > 0);

    // Parse the JSON response
    json_response = parse_json(pszOutBuffer);
    if (json_response) {
        result = find_content(json_response);
    }

cleanup:
    // Clean up resources
    if (hRequest) WinHttpCloseHandle(hRequest);
    if (hConnect) WinHttpCloseHandle(hConnect);
    if (hSession) WinHttpCloseHandle(hSession);
    if (pszOutBuffer) free(pszOutBuffer);
    if (post_fields) free(post_fields);
    if (request) free_json(request);
    if (json_response) free_json(json_response);

    return result;
}

#else
struct MemoryStruct {
    char *memory;
    size_t size;
};

static size_t WriteMemoryCallback(void *contents, size_t size, size_t nmemb, void *userp) {
    size_t realsize = size * nmemb;
    struct MemoryStruct *mem = (struct MemoryStruct *)userp;

    // Check for potential overflow
    if (SIZE_MAX - mem->size < realsize) {
        fprintf(stderr, "Cannot allocate memory, size_t overflow detected\n");
        return 0;
    }

    char *ptr = reallocx(mem->memory, mem->size + realsize + 1);

    mem->memory = ptr;
    memcpy(&(mem->memory[mem->size]), contents, realsize);
    mem->size += realsize;
    mem->memory[mem->size] = 0;

    return realsize;
}
char* chatgpt_unix(const char* prompt, char *api_key) {
    CURL* curl = NULL;
    CURLcode res;
    struct MemoryStruct chunk = { .memory = NULL, .size = 0 };
    struct curl_slist* headers = NULL;
    char* result = NULL;
    char* post_fields = NULL;
    JsonValue* request = NULL;

    // Initialize memory for chunk
    chunk.memory = allocx(1);
    chunk.size = 0;

    curl_global_init(CURL_GLOBAL_ALL);
    curl = curl_easy_init();

    if (!curl) {
        fprintf(stderr, "curl_easy_init() failed\n");
        goto cleanup;
    }

    char auth_header[100];
    // Use snprintf for safe string formatting
    snprintf(auth_header, sizeof(auth_header), "Authorization: Bearer %s", api_key);
    headers = curl_slist_append(headers, auth_header);
    if (!headers) {
        fprintf(stderr, "curl_slist_append() failed\n");
        goto cleanup;
    }

    headers = curl_slist_append(headers, "Content-Type: application/json");
    if (!headers) {
        fprintf(stderr, "curl_slist_append() failed\n");
        goto cleanup;
    }

    // Create JSON object for the request
    request = create_object();
    if (!request) {
        fprintf(stderr, "Memory allocation failed\n");
        goto cleanup;
    }

    add_to_object(request, "model", create_string("gpt-4o-mini"));
    
    JsonValue* messages = create_array();
    if (!messages) {
        fprintf(stderr, "Memory allocation failed\n");
        goto cleanup;
    }

    JsonValue* message = create_object();
    if (!message) {
        fprintf(stderr, "Memory allocation failed\n");
        goto cleanup;
    }

    add_to_object(message, "role", create_string("user"));
    add_to_object(message, "content", create_string(prompt));
    add_to_array(messages, message);
    add_to_object(request, "messages", messages);

    post_fields = serialize_json(request);
    if (!post_fields) {
        fprintf(stderr, "JSON serialization failed\n");
        goto cleanup;
    }

    curl_easy_setopt(curl, CURLOPT_URL, "https://api.openai.com/v1/chat/completions");
    curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
    curl_easy_setopt(curl, CURLOPT_POSTFIELDS, post_fields);
    curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteMemoryCallback);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void*)&chunk);

    res = curl_easy_perform(curl);

    if (res != CURLE_OK) {
        fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        goto cleanup;
    }

    JsonValue* json = parse_json(chunk.memory);
    if (json) {
        result = find_content(json);
        free_json(json);
    }

cleanup:
    // Free resources in reverse order of allocation
    if (request) free_json(request);
    if (post_fields) free(post_fields);
    if (chunk.memory) free(chunk.memory);
    if (headers) curl_slist_free_all(headers);
    if (curl) curl_easy_cleanup(curl);
    curl_global_cleanup();

    return result;
}

#endif

// Wrapper function to call the appropriate implementation
char* chatgpt(const char* prompt, char* api_key) {
#ifdef _WIN32
    return chatgpt_windows(prompt, api_key);
#else
    return chatgpt_unix(prompt, api_key);
#endif
}

char* chatgpt_env_key(const char* prompt) {
    char* api_key = getenv("OPENAI_API_KEY");
    if (!api_key) {
        fprintf(stderr, "OPENAI_API_KEY environment variable not set\n");
	return NULL;
    }

    return chatgpt(prompt, api_key);
}
