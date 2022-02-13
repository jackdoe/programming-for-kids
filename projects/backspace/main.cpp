#include <windows.h>
#include <iostream>


using namespace std;

HHOOK hHook = 0;
static bool ctrlPressed = false;
static bool replacementPressed = false;
static bool fake = false;
static bool ctrlUnpressed = false;

struct alias {
    BYTE bVk;
    BYTE bScan;
};

static struct alias replacement = { 0 };

LRESULT CALLBACK LowLevelKeyboardProc(int nCode, WPARAM wParam, LPARAM lParam) {
    if (!fake && nCode == HC_ACTION && wParam != WM_SYSKEYUP && wParam != WM_SYSKEYDOWN) {
        KBDLLHOOKSTRUCT* p = (KBDLLHOOKSTRUCT*)lParam;

        if (p->scanCode == 0x1d) {
            ctrlPressed = wParam == WM_KEYDOWN;
        }
     
        if (ctrlPressed) {
            if (p->scanCode == 0x23 || p->scanCode == 0x24) {
                if (p->scanCode == 0x23) { 
                    // ctrl+h -> backspace
                    replacement.bVk = VK_BACK;
                    replacement.bScan = 0x0e;
                }
                else {
                    // ctrl+j -> return
                    replacement.bVk = VK_RETURN;
                    replacement.bScan = 0x1c;
                }

                fake = true;

                /*
                    in order to work with the following sequence:
                    ctrl down
                        h down
                        h down (hold)
                        h up
                        j down
                        j down (hold)
                        j up
                        p down
                        p up
                    ctrl up
                    we need to put ctrl back down to support ctrl+h followed by ctrl+p and vice versa
                */
                
                if (wParam == WM_KEYUP) {
                    keybd_event(replacement.bVk, replacement.bScan, KEYEVENTF_KEYUP, 0);
                    keybd_event(VK_CONTROL, 0x1d, 0, 0);
                    ctrlUnpressed = false;
                    replacementPressed = false;
                }
                else {
                    // h is down and control was pressed, first we 
                    // need to unpress control otherwise we will send 
                    // ctrl+backspace which deletes the whole word
                    if (!ctrlUnpressed) {
                        // leave control unpressed for repeated ctrl+h
                        // we will press it back if something ch
                        // we have this global var to not reenter LowLevelKeyboardProcp
                        keybd_event(VK_CONTROL, 0x1d, KEYEVENTF_KEYUP, 0);
                        ctrlUnpressed = true;
                    }

                    keybd_event(replacement.bVk, replacement.bScan, 0, 0);
                    replacementPressed = true;
                }
                fake = false;
                return 1;
            }
        }
        else if (replacementPressed) {
            fake = true;
            keybd_event(replacement.bVk, replacement.bScan, KEYEVENTF_KEYUP, 0);
            replacementPressed = false;
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