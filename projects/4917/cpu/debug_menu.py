INSTRUCTIONSET_HELP = """
0 HALT
1 R0 = R0 + R1 (add R0 and R1 and store the result in R0)
2 R0 = R0 - R1 (subtract R0 and R1 and store the result in R0)
3 R0 = R0 + 1  (increment R0)
4 R1 = R1 + 1  (increment R1)
5 R0 = R0 - 1  (decrement R0)
6 R1 = R1 - 1  (decrement R1)
7 BEEP

8 X PRINT X (print the next memory cell)

9 X R0 = MEMORY[X] (load the value of address X into R0)
10 X R1 = MEMORY[X] (load the value of address X into R1)
11 X MEMORY[X] = R0 (store the value of R0 into address X)
12 X MEMORY[X] = R1 (store the value of R1 into address X)

13 X JUMP X (jump to the value in the next memory cell)
     e.g. 13 7 means jump to address 7
14 X JUMP X IF R0 == 0 (jump to X if R0 is equal to 0)
     e.g. 14 7 means jump to address 7 if R0 is equal to 0
     otherwise proceed with the next instruction
15 X JUMP X IF R0 != 0 (jump to X if R0 is *not* equal to 0)

You see some of the instructions take 1 memory cell, like INCREMENT or
BEEP, but others take two cells like PRINT or JUMP.

You can also see that it cant just go and do addition or subtraction
directly in memory, first it needs to load the values from memory into
R0 and R1 and then do addition and then put it back in memory.

The JUMP instructions are also called BRANCH instructions, BRANCH,
BRANCH IF ZERO, BRANCH IF NOT ZERO or B, BZ, BNZ for short.
"""


def prompt_number(prompt, default=None):
    while True:
        inp = input(f"{prompt}: ").strip()
        if inp:
            num = 0
            try:
                num = int(inp)
                if 0 <= num < 16:
                    break
                else:
                    raise Exception()
            except:
                print("Enter a number between 0 and 15.")
        elif default:
            num = default
            break
    return num


def change_memory(memory):
    address = prompt_number("\nAddress")
    value = memory[address]
    value = prompt_number(f"Value, now [{value}]", value)
    memory[address] = value
    return memory


def change_state(IP, R0, R1, memory):
    while True:
        print(
            f"""
1. Change IP, now [{IP}]
2. Change R0, now [{R0}]
3. Change R1, now [{R1}]
4. Memory, now {memory}
q. Quit
    """
        )
        inp = input("Enter your choice: ").strip().lower()
        if inp == "1":
            IP = prompt_number("IP")
        elif inp == "2":
            R0 = prompt_number("R0")
        elif inp == "3":
            R0 = prompt_number("R1")
        elif inp == "4":
            memory = change_memory(memory)
        elif inp == "q":
            break
    return IP, R0, R1, memory


def debug_more_menu(IP, R0, R1, memory, visualize):
    while True:
        print(
            f"""
1. Toggle visualizer, now [{visualize}]
2. List intruction set
3. Change CPU state
q. Quit
"""
        )
        inp = input("Your choice: ").strip().lower()
        if inp == "1":
            visualize = "asm" if visualize == "matrix" else "matrix"
            break
        elif inp == "2":
            print(INSTRUCTIONSET_HELP)
        elif inp == "3":
            IP, R0, R1, memory = change_state(IP, R0, R1, memory)
        elif inp == "q":
            break
    return IP, R0, R1, memory, visualize
