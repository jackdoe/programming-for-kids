#include <dsound.h>
#include <math.h>
#include <mmsystem.h>
#include <stdint.h>
#include <time.h>
#include <windows.h>

#include <cstdio>

typedef int8_t int8;
typedef int16_t int16;
typedef int32_t int32;
typedef int64_t int64;
typedef uint8_t uint8;
typedef uint16_t uint16;
typedef uint32_t uint32;
typedef uint64_t uint64;
typedef int32 bool32;
typedef float real32;
typedef double real64;

#define Pi32 3.14159265359

#define panic(fmt, arg...)                                                  \
    do {                                                                    \
        printf(fmt " [%s():%s:%d]\n", ##arg, __func__, __FILE__, __LINE__); \
        exit(EXIT_FAILURE);                                                 \
    } while (0);

// copy pasta from chatgpt: how to alphablend two 32 bit pixels in c
uint32_t alpha_blend(uint32_t pixel1, uint32_t pixel2) {
    // Extract the alpha, red, green, and blue values for each pixel
    uint8_t alpha1 = (pixel1 >> 24) & 0xFF;
    uint8_t red1 = (pixel1 >> 16) & 0xFF;
    uint8_t green1 = (pixel1 >> 8) & 0xFF;
    uint8_t blue1 = pixel1 & 0xFF;

    uint8_t alpha2 = (pixel2 >> 24) & 0xFF;
    uint8_t red2 = (pixel2 >> 16) & 0xFF;
    uint8_t green2 = (pixel2 >> 8) & 0xFF;
    uint8_t blue2 = pixel2 & 0xFF;

    // Calculate the alpha blending factors
    float alpha_factor1 = (float)alpha1 / 255.0f;
    float alpha_factor2 = (float)alpha2 / 255.0f;

    // Calculate the blended color values
    float blended_red = (1 - alpha_factor1) * red2 + alpha_factor1 * red1;
    float blended_green = (1 - alpha_factor1) * green2 + alpha_factor1 * green1;
    float blended_blue = (1 - alpha_factor1) * blue2 + alpha_factor1 * blue1;

    // Convert the blended color values to 8-bit integers and pack them into a 32-bit pixel value
    uint32_t blended_pixel = ((uint32_t)(alpha1) << 24) |
                             ((uint32_t)(blended_red) << 16) |
                             ((uint32_t)(blended_green) << 8) |
                             (uint32_t)(blended_blue);

    return blended_pixel;
}
struct keyboard {
    bool32 UP;
    bool32 DOWN;
    bool32 LEFT;
    bool32 RIGHT;
    bool32 SPACE;
    bool32 W;
    bool32 A;
    bool32 S;
    bool32 D;
};

struct screen_buffer {
    void* Memory;
    BITMAPINFO Info;
    int Width;
    int Height;
};

struct win32_window_dimension {
    int Width;
    int Height;
};

bool GlobalRunning = true;
keyboard GlobalKeyboard;

win32_window_dimension Win32GetWindowDimension(HWND Window) {
    win32_window_dimension Result;
    RECT ClientRect;
    GetClientRect(Window, &ClientRect);
    Result.Width = ClientRect.right - ClientRect.left;
    Result.Height = ClientRect.bottom - ClientRect.top;
    return Result;
}

struct rect {
    int x;
    int y;
    int width;
    int height;
    uint32 color;
};
inline int min(int a, int b) {
    if (a < b) return a;
    return b;
}
inline int max(int a, int b) {
    if (a > b) return a;
    return b;
}
// 0 10 300
inline int between(int a, int b, int c) {
    return max(min(b, c), a);
}
void rect_draw(struct rect r, screen_buffer* buf) {
    for (int y = r.y; y < r.y + r.height; y++) {
        if (y >= buf->Height || y <= 0) continue;
        uint32 off = y * buf->Width + r.x;
        uint32* pixel = (uint32*)buf->Memory + off;

        for (int x = r.x; x < r.x + r.width; x++, pixel++) {
            if (x >= buf->Width || x <= 0) continue;

            *pixel = alpha_blend(r.color, *pixel);
        }
    }
}

void screen_clear(screen_buffer* Buffer, uint32 color) {
    uint32* pixel = (uint32*)Buffer->Memory;
    for (int i = 0; i < Buffer->Width * Buffer->Height; i++) {
        *pixel++ = color;
    }
    // memset(Buffer->Memory, 0, Buffer->Width * Buffer->Height * 4);
}

void Win32ResizeDIBSection(screen_buffer* Buffer,
                           int Width,
                           int Height) {
    if (Buffer->Memory) {
        VirtualFree(Buffer->Memory, 0, MEM_RELEASE);
    }

    Buffer->Width = Width;
    Buffer->Height = Height;

    Buffer->Info.bmiHeader.biSize = sizeof(Buffer->Info.bmiHeader);
    Buffer->Info.bmiHeader.biWidth = Buffer->Width;
    Buffer->Info.bmiHeader.biHeight = -Buffer->Height;
    Buffer->Info.bmiHeader.biPlanes = 1;
    Buffer->Info.bmiHeader.biBitCount = 4 * 8;
    Buffer->Info.bmiHeader.biCompression = BI_RGB;

    int BitmapSize = Buffer->Width * Buffer->Height * 4;

    Buffer->Memory =
        VirtualAlloc(0, BitmapSize, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
}

void Win32UpdateWindow(HDC DeviceContext,
                       int WindowWidth,
                       int WindowHeight,
                       screen_buffer* Buffer) {
    StretchDIBits(DeviceContext, 0, 0, WindowWidth, WindowHeight,  // dest
                  0, 0, Buffer->Width, Buffer->Height,             // src
                  Buffer->Memory, &Buffer->Info, DIB_RGB_COLORS, SRCCOPY);
}

LRESULT CALLBACK Win32MainWindowCallback(HWND Window,
                                         UINT Message,
                                         WPARAM WParam,
                                         LPARAM LParam) {
    LRESULT Result = 0;
    switch (Message) {
        case WM_ACTIVATEAPP: {
            OutputDebugStringA("WM_ACTIVATEAPP\n");
        } break;

        case WM_CLOSE: {
            GlobalRunning = false;
            OutputDebugStringA("WM_CLOSE\n");
        } break;

        case WM_DESTROY: {
            OutputDebugStringA("WM_DESTROY\n");
        } break;

        case WM_SYSKEYUP:
        case WM_SYSKEYDOWN:
        case WM_KEYUP:
        case WM_KEYDOWN: {
            uint32 VKCode = WParam;
            bool32 WasDown = LParam & (1 << 30);
            bool32 IsDown = LParam & (1 << 31);
            int keyboardScanCode = (LParam >> 16) & 0x00ff;

            switch (VKCode) {
                case VK_F4: {
                    bool32 IsAltDown = LParam & (1 << 29);
                    if (IsAltDown) {
                        GlobalRunning = false;
                    }
                } break;

                case VK_UP: {
                    GlobalKeyboard.UP = !IsDown;
                } break;

                case VK_DOWN: {
                    GlobalKeyboard.DOWN = !IsDown;
                } break;

                case VK_LEFT: {
                    GlobalKeyboard.LEFT = !IsDown;
                } break;

                case VK_RIGHT: {
                    GlobalKeyboard.RIGHT = !IsDown;
                } break;
            }

            switch (VKCode) {
                case 32:
                    GlobalKeyboard.SPACE = !IsDown;
                    break;
                case 87:
                    GlobalKeyboard.W = !IsDown;
                    break;
                case 65:
                    GlobalKeyboard.A = !IsDown;
                    break;
                case 83:
                    GlobalKeyboard.S = !IsDown;
                    break;
                case 68:
                    GlobalKeyboard.D = !IsDown;
                    break;
            }
        } break;

        case WM_SIZE: {
            OutputDebugStringA("WM_SIZE\n");
        } break;

        default: {
            Result = DefWindowProcA(Window, Message, WParam, LParam);
        } break;
    }

    return Result;
}

void wait(LARGE_INTEGER freq, float ms) {
    LARGE_INTEGER t1, t2, t3;
    float elapsed = 0;
    QueryPerformanceCounter(&t1);
    do {
        Sleep(ms / 2);
        QueryPerformanceCounter(&t2);
        elapsed =
            ((float)(t2.QuadPart - t1.QuadPart) * 1000.0) / (float)freq.QuadPart;

    } while (ms > elapsed);
}
int CALLBACK initialize(HINSTANCE Instance,
                        const char* windowsName,
                        void update(struct keyboard*),
                        void draw(struct screen_buffer*)) {
    WNDCLASS WindowClass = {};

    WindowClass.style = CS_HREDRAW | CS_VREDRAW;

    WindowClass.lpfnWndProc = Win32MainWindowCallback;
    WindowClass.hInstance = Instance;
    WindowClass.lpszClassName = windowsName;

    if (!RegisterClass(&WindowClass))
        panic("RegisterClass");

    int width = 1024;
    int height = 768;

    HWND Window = CreateWindowEx(0, windowsName, windowsName,
                                 WS_OVERLAPPEDWINDOW | WS_VISIBLE, CW_USEDEFAULT,
                                 CW_USEDEFAULT, width, height, 0, 0, Instance, 0);

    if (!Window)
        panic("CreateWindowEx");

    struct screen_buffer screen;

    Win32ResizeDIBSection(&screen, width, height);

    LARGE_INTEGER frequency;
    LARGE_INTEGER t1, t2, t3;
    float elapsedTimeBeforeSleep, elapsedTimeWithSleep;
    QueryPerformanceFrequency(&frequency);

    HDC DeviceContext = GetDC(Window);
    win32_window_dimension dimension = Win32GetWindowDimension(Window);
    while (GlobalRunning) {
        QueryPerformanceCounter(&t1);

        MSG message = {};
        SetCursor(NULL);
        while (PeekMessage(&message, 0, 0, 0, PM_REMOVE)) {
            TranslateMessage(&message);
            DispatchMessage(&message);
        }

        update(&GlobalKeyboard);
        draw(&screen);

        Win32UpdateWindow(DeviceContext, screen.Width, screen.Height, &screen);

        QueryPerformanceCounter(&t2);
        elapsedTimeBeforeSleep =
            ((float)(t2.QuadPart - t1.QuadPart) * 1000.0 / frequency.QuadPart);
        float sleep = 16 - elapsedTimeBeforeSleep;
        if (sleep > 0) {
            wait(frequency, sleep);
        }

        QueryPerformanceCounter(&t3);
        elapsedTimeWithSleep =
            ((float)((t3.QuadPart - t1.QuadPart) * 1000.0) / frequency.QuadPart);
        /*
            printf("%f, slept: %f, actual elapsed: %f %lld\n",
           elapsedTimeBeforeSleep, sleep, elapsedTimeWithSleep, (t3.QuadPart -
           t1.QuadPart) / frequency.QuadPart);
                   */
    }
    ReleaseDC(Window, DeviceContext);

    return 0;
}

struct bitmap_image {
    struct rect r;
    uint32* pixels;
};
// taken from stackoverflow
struct bitmap_image bitmap_read_file(const char* filename) {
    FILE* file = fopen(filename, "rb");
    if (!file) panic("file");

    BITMAPFILEHEADER fileHeader;
    size_t readn;
    readn = fread(&fileHeader, sizeof(BITMAPFILEHEADER), 1, file);
    if (readn != 1) panic("fread: %d vs %d", readn, sizeof(BITMAPFILEHEADER));

    BITMAPINFOHEADER infoHeader;
    readn = fread(&infoHeader, sizeof(BITMAPINFOHEADER), 1, file);
    if (readn != 1) panic("fread: %d vs %d", readn, sizeof(BITMAPINFOHEADER));

    int width = infoHeader.biWidth;
    int height = infoHeader.biHeight;
    int colorDepth = infoHeader.biBitCount;
    int imageSize = width * height * (colorDepth / 8);
    uint8* data = (uint8*)malloc(imageSize);
    if (!data)
        panic("memory");
    uint32* pixels = (uint32*)malloc(width * height * 4);
    if (!pixels)
        panic("memory");

    fseek(file, fileHeader.bfOffBits, SEEK_SET);
    fread(data, imageSize, 1, file);
    fclose(file);

    if (colorDepth == 24) {
        int n = 0;
        for (int i = 0; i < imageSize; i += 3) {
            uint8 red = data[i + 2];
            uint8 green = data[i + 1];
            uint8 blue = data[i];
            pixels[n++] = (uint32)255 << 24 | (uint32)red << 16 | (uint32)green << 8 | (uint32)blue;
        }
    } else if (colorDepth == 32) {
        int n = 0;
        for (int i = 0; i < imageSize; i += 4) {
            uint8 red = data[i + 2];
            uint8 green = data[i + 1];
            uint8 blue = data[i];
            uint8 alpha = data[i + 3];
            pixels[n++] = (uint32)alpha << 24 | (uint32)red << 16 | (uint32)green << 8 | (uint32)blue;
        }
    } else {
        panic("unsupported colordepth: %d", colorDepth)
    }

    struct bitmap_image bi = {0};
    bi.r.width = width;
    bi.r.height = height;
    bi.pixels = pixels;
    return bi;
}

void bitmap_draw(struct bitmap_image b, screen_buffer* buf) {
    int bitmapOffY = b.r.height - 1;

    for (int y = b.r.y; y < b.r.y + b.r.height; y++, bitmapOffY--) {
        if (y >= buf->Height || y <= 0) continue;

        uint32 off = y * buf->Width + b.r.x;
        uint32* pixel = (uint32*)buf->Memory + off;
        int bitmapOffX = 0;
        for (int x = b.r.x; x < b.r.x + b.r.width; x++, bitmapOffX++, pixel++) {
            if (x >= buf->Width || x <= 0) continue;

            uint32 v = *(b.pixels + (bitmapOffY * b.r.width) + bitmapOffX);
            *pixel = alpha_blend(*pixel, v);
        }
    }
}

// copy pasta from chatgpt: check if two rectangle structs with x,y, width, height overlap
int collide(struct rect rect1, struct rect rect2) {
    if (!(rect1.x + rect1.width < rect2.x || rect2.x + rect2.width < rect1.x) && !(rect1.y + rect1.height < rect2.y || rect2.y + rect2.height < rect1.y)) {
        return 1;
    }
    return 0;
}

time_t start = 0;
void play(const char* fn) {
    time_t now = time(0);
    if (now - start > 1) {
        PlaySound(fn, NULL, SND_ASYNC);
        start = now;
    }
}