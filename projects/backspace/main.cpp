#include <windows.h>
#include <iostream>

using namespace std;

HHOOK hHook = 0;
static bool ctrlPressed = false;
static bool backspacePressed = false;
static bool fake = false;
static bool ctrlUnpressed = false;


LRESULT CALLBACK LowLevelKeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (!fake && nCode == HC_ACTION && wParam != WM_SYSKEYUP && wParam != WM_SYSKEYDOWN) {
        KBDLLHOOKSTRUCT* p = (KBDLLHOOKSTRUCT*)lParam;

        if (p->scanCode == 0x1d) {
            ctrlPressed = wParam == WM_KEYDOWN;
        }
        /*
            in order to work with the following sequence:

            ctrl down
                h down
                h down
                h up
                p down
                p up
            ctrl up

            we need to put ctrl back down to support ctrl+h followed by ctrl+p
        */
     
        if (ctrlPressed) {
            if (p->scanCode == 0x23) {
                fake = true;
                // h is up
                if (wParam == WM_KEYUP) {
                    // unpress backspace
                    // press control
                    keybd_event(VK_BACK, 0x0e, KEYEVENTF_KEYUP, 0);
                    keybd_event(VK_CONTROL, 0x1d, 0, 0);
                    ctrlUnpressed = false;
                    backspacePressed = false;
                }
                else {
                    // h is down and control was pressed, first we 
                    // need to unpress control otherwise we will send 
                    // ctrl+backspace which deletes whole word
                    if (!ctrlUnpressed) {
                        // leave control unpressed for repeated ctrl+h
                        // we will press it back if something ch
                        // we have this global var to not reenter LowLevelKeyboardProcp
                        keybd_event(VK_CONTROL, 0x1d, KEYEVENTF_KEYUP, 0);
                        ctrlUnpressed = true;
                    }
                    keybd_event(VK_BACK, 0x0e, 0, 0);
                    backspacePressed = true;
                }
                fake = false;
                return 1;
            }
        }
        else if (backspacePressed) {
            fake = true;
            keybd_event(VK_BACK, 0x0e, KEYEVENTF_KEYUP, 0);
            backspacePressed = false;
            fake = false;
        }
    }
    return CallNextHookEx(hHook, nCode, wParam, lParam);
}
int WINAPI WinMain(HINSTANCE hThisInstance, HINSTANCE hPrevInstance, LPSTR lpszArgument, int nCmdShow) {
    hHook = SetWindowsHookEx(WH_KEYBOARD_LL, &LowLevelKeyboardProc, hThisInstance, NULL);
    if (hHook == NULL) {
        return 1;
    }

    MSG messages;

    while (GetMessage(&messages, NULL, 0, 0)) {
        TranslateMessage(&messages);
        DispatchMessage(&messages);
    }

    return messages.wParam;
}