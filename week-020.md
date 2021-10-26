## [DAY-136] For; Arrays; Memory

Lets make a super simple C program

Just to get familiar witht he syntax, it does not use indentation to group code, but {}, and also each variable has to have known type (size), e.g we have to tell the C compiler (compiler is a program that takes the text code and transforms it into machine code) that  `i` is of type `int` which on our computer is exactly 4 bytes long.

```
#include <stdio.h>
int main() {
    int sum = 0;
    for (int i = 0; i < 100; i++) {
        sum += 10;
    }

    printf("%d\n", sum);
}
```

When you execute `gcc -o foo foo.c` (if you save the program in foo.c), it will make the binary `foo`, do `cat foo` to see the actual binary made from the compiler. If you run `objdump -D foo` you will see the assembly code and the machine code corresponding to it.

`cat foo`:
```
????X? H__PAGEZERO?__TEXT@@__text__TEXT0?X0??__stubs__TEXT????__stub_helper__TEXT?????__cstring__TEXT????__unwind_info__TEXT??H???__DATA_CONST@@@@__got__DATA_CONST@?__DATA?@?@__la_symbol_ptr__DATA?__data__DA?H__LINKEDIT?@?"?? ?0?0h???H
                               P?? 
                                   /usr/lib/dyld9??
                                                   f:^?[c?υ02 

                                                              ?*(?0?
                                                                    8d
                                                                      /usr/lib/libSystem.B.dylib&`)h?UH??H???E??E??E??}?d??E???
?E??E???E???????u?H?=2??	?E?H??]??%r@L?q@AS?%a?h?????%d
0?44??4
       ??#Q@dyld_stub_binderQr?s@_printf?__mh_execute_header!main%?~??0?$ __mh_execute_header_main_printfdyld_stub_binder__dyld_privat
```

Because its a binary file, most of the bytes are not actually printable ASCII characters, you can use `hexdump` to see the byte's values:

`hexdump -C foo`

```
00000000  cf fa ed fe 07 00 00 01  03 00 00 00 02 00 00 00  |................|
00000010  10 00 00 00 58 05 00 00  85 00 20 00 00 00 00 00  |....X..... .....|
00000020  19 00 00 00 48 00 00 00  5f 5f 50 41 47 45 5a 45  |....H...__PAGEZE|
00000030  52 4f 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |RO..............|
00000040  00 00 00 00 01 00 00 00  00 00 00 00 00 00 00 00  |................|
00000050  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000060  00 00 00 00 00 00 00 00  19 00 00 00 d8 01 00 00  |................|
00000070  5f 5f 54 45 58 54 00 00  00 00 00 00 00 00 00 00  |__TEXT..........|
00000080  00 00 00 00 01 00 00 00  00 40 00 00 00 00 00 00  |.........@......|
00000090  00 00 00 00 00 00 00 00  00 40 00 00 00 00 00 00  |.........@......|
000000a0  05 00 00 00 05 00 00 00  05 00 00 00 00 00 00 00  |................|
000000b0  5f 5f 74 65 78 74 00 00  00 00 00 00 00 00 00 00  |__text..........|
000000c0  5f 5f 54 45 58 54 00 00  00 00 00 00 00 00 00 00  |__TEXT..........|
000000d0  30 3f 00 00 01 00 00 00  58 00 00 00 00 00 00 00  |0?......X.......|
000000e0  30 3f 00 00 04 00 00 00  00 00 00 00 00 00 00 00  |0?..............|
000000f0  00 04 00 80 00 00 00 00  00 00 00 00 00 00 00 00  |................|
00000100  5f 5f 73 74 75 62 73 00  00 00 00 00 00 00 00 00  |__stubs.........|
00000110  5f 5f 54 45 58 54 00 00  00 00 00 00 00 00 00 00  |__TEXT..........|
00000120  88 3f 00 00 01 00 00 00  06 00 00 00 00 00 00 00  |.?..............|
00000130  88 3f 00 00 01 00 00 00  00 00 00 00 00 00 00 00  |.?..............|
00000140  08 04 00 80 00 00 00 00  06 00 00 00 00 00 00 00  |................|

[...]

```

`objdump -D foo`
```
[...]
100003f30: 55                           pushq   %rbp
100003f31: 48 89 e5                     movq    %rsp, %rbp
100003f34: 48 83 ec 10                  subq    $16, %rsp
100003f38: c7 45 fc 00 00 00 00         movl    $0, -4(%rbp)
100003f3f: c7 45 f8 00 00 00 00         movl    $0, -8(%rbp)
100003f46: c7 45 f4 00 00 00 00         movl    $0, -12(%rbp)
100003f4d: 83 7d f4 64                  cmpl    $100, -12(%rbp)
100003f51: 0f 8d 17 00 00 00            jge     0x100003f6e <_main+0x3e>
100003f57: 8b 45 f8                     movl    -8(%rbp), %eax
100003f5a: 83 c0 0a                     addl    $10, %eax
100003f5d: 89 45 f8                     movl    %eax, -8(%rbp)
100003f60: 8b 45 f4                     movl    -12(%rbp), %eax
100003f63: 83 c0 01                     addl    $1, %eax
100003f66: 89 45 f4                     movl    %eax, -12(%rbp)
100003f69: e9 df ff ff ff               jmp     0x100003f4d <_main+0x1d>
[...]
```

`addl` meand `add`, `jmp` means jump and so forth. This is not important for now, the point is that `gcc` which is a popular C compiler, will take your code and make it into machine code.

Lets have another example:


FizzBuzz

```
#include <stdio.h>
int main() {
    for (int i = 0; i < 100; i++) {
        if (i % 15 == 0) {
            printf("fizzbuzz\n");
        } else if (i % 5 == 0) {
            printf("buzz\n");
        } else if (i % 3 == 0) {
            printf("fizz\n");
        } else {
            printf("%d\n",i);
        }
    }
}
```

What is your name?

```
#include <stdio.h>
int main() {
    char input[20] = {0};
    while(1) {
        printf("What is your name: ");
        scanf("%s",input);
        printf("\nHello %s\n",input);
    }
}
```

You see how we say `char input[20]` which means we habe 20 elements of type `char` pointed by the input variable, it is literally just a pointer to some memory, and we can use `input[1]` to go to the address `input` plus 1 byte. Same with `int x[10]`, if we do x[3], it will go to the address pointed by `x` and add 3 * 4 to it.

We can make interesting bugs like that, because nobody will check if we go and read somewhere outside of the defined array:


```
#include <stdio.h>
int main() {
    char input[20] = {0};
    int b = 5;
    while(1) {
        printf("What is your name: ");
        scanf("%s",input);
        printf("\nHello %s\n",input);

        for (int i = 0; i < 40; i++) {
            printf("  %d -> %d -> %c\n", i, input[i],input[i]);
        }
    }
}

```

You will see some garbage from element 20 to 39, because it will actually go and read beyond the input bounderioes.
