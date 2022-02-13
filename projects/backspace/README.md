For fast touchtyping you need access to backspace, on Windows you cant make it to support ctrl+h propelry, maybe you can install AutoKey or something, but I felt a bit too vulnerable to use someone else's program to control my keyboard.

My daughter is 10, and her hands are small, so when she goes to hit the backspace it is just too far. I thought it is good tine to teach her to use ctrl+h and ctrl+j (enter is quite far for her pinky as well).

So I wrote a quick thing to capture ctrl+h and send backspace instead of ctrl+h, this way it works everywhere.

Download the compiled program at your own risk, as it is just few bytes away from being a keylogger, I put it here just for my convenience, but I strongly recommend you compile it yourself (install Visual Studio 2022 and make new project and just put main.cpp there).

The SHA256 sum at time of uploading is:

```
466607e8c755d5ac9f5f55ba81bb07cbcab5423053acf86c96ff426c61edb409  Backspace.exe
```

If you want it to start automatically, put Backapace.exe in `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`