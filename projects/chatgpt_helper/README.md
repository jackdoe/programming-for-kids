Sonnet3.5 wrote this, it must be with quite some bugs and leaks, dont use it besises to just play with it

Example usage:

```
#include "chatgpt.h"
int main() {
    const char* prompt = "Hello, how are you?";
    char* response = chatgpt_env_key(prompt);

    if (response) {
        printf("Response from GPT: %s\n", response);
        free(response);
    } else {
        printf("Failed to get a response from GPT.\n");
    }

    return 0;
}
```


Compile with:

```
$ gcc -o main chatgpt.c -lcurl
./main 
Response from GPT: Hello! I'm just a program, but I'm here and ready to help you. How can I assist you today?
```

