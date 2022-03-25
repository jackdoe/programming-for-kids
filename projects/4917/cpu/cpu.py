import time
from enum import Enum, auto

from cpu.instruction_set import InstructionType, instruction_set
from cpu.ascii_visualizer import ascii
from cpu.disassembler import disassemble

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


class DebugAction(Enum):
    CONTINUE = auto()
    QUIT = auto()
    TOGGLE_VISUALIZER = auto()
    SHOW_INSTRUCTION_SET = auto()
    REFRESH = auto()


def prompt_number(prompt):
    while True:
        print("\nEnter a number between 0 and 16:")
        inp = input(f"{prompt}: ").strip()
        if inp:
            num = 0
            try:
                num = int(inp)
                if not (0 <= num < 16):
                    raise Exception()
                break
            except:
                pass
    return num


def change_state(IP, R0, R1, memory):
    print("\nEnter a letter or digit indicating the state value to change:")
    while True:
        inp = (
            input(
                f"i => IP[{IP}] 0 => R0[{R0}] 1 => R1[{R1}] m => memory q => quit: [i,0,1,m,q]? "
            )
            .strip()
            .lower()
        )
        if not inp or inp == "q":
            break
        if inp == "i":
            IP = prompt_number(f"IP[{IP}]")
        elif inp == "0":
            R0 = prompt_number(f"R0[{R0}]")
        elif inp == "1":
            R0 = prompt_number(f"R1[{R1}]")
    return IP, R0, R1, memory


def debug_prompt(IP, R0, R1, memory):
    action = None
    while not action:
        inp = input("hit enter to continue or 'q' enter to quit> ")
        inp = inp.strip().lower()
        if inp == "q":
            action = DebugAction.QUIT
        elif inp == "t":
            action = DebugAction.TOGGLE_VISUALIZER
        elif inp == "i":
            print(INSTRUCTIONSET_HELP)
            action = DebugAction.REFRESH
        elif inp == "s":
            IP, R0, R1, memory = change_state(IP, R0, R1, memory)
            action = DebugAction.REFRESH
        else:
            action = DebugAction.CONTINUE
    return IP, R0, R1, memory, action


def exec_instruction(state):
    IP, IS, R0, R1, memory = state

    # Lookup the function to execute and the width of the instruction
    microcode, type = instruction_set[IS]

    if type is InstructionType.REGISTER:
        # register instruction
        R0, R1 = microcode(R0, R1)
    elif type is InstructionType.MEMORY:
        # memory instruction
        R0, R1, memory = microcode(R0, R1, IP, memory)
        IP += 1
    elif type is InstructionType.BRANCH:
        # branch instruction
        IP = microcode(IP, R0, memory)
    elif type is InstructionType.STATELESS:
        # stateless instruction
        microcode()
    else:
        raise Exception(f"Invalid instruction type: {type}")

    # truncate registers to 4 bits (all are unsigned nibbles)
    IP, R0, R1 = (register & 0xF for register in (IP, R0, R1))

    return IP, IS, R0, R1, memory


def cpu(visualize, memory, IP=0, R0=0, R1=0, debug=True):
    cycle = 0
    quit = False
    visualizer = ascii if visualize == "matrix" else disassemble
    refresh = False

    while True:
        # Fetch the next instruction
        IS = memory[IP]

        highlight = [IP]
        if IS >= 8:
            highlight = [IP, (IP + 1) & 0xF]

        if debug:
            visualizer = ascii if visualize == "matrix" else disassemble
            visualizer((IP, IS, R0, R1, memory), highlight, cycle)
            IP, R0, R1, memory, action = debug_prompt(IP, R0, R1, memory)
            # inp = input("hit enter to continue or 'q' enter to quit> ")
            if action is DebugAction.QUIT:
                quit = True
                break
            elif action is DebugAction.TOGGLE_VISUALIZER:
                # toggle visualizer
                visualize = "asm" if visualize == "matrix" else "matrix"
                refresh = True
            elif action is DebugAction.REFRESH:
                refresh = True
            else:
                print()
        else:
            time.sleep(0.1)

        if refresh:
            refresh = False
        else:
            # Increment the instruction pointer
            IP = (IP + 1) & 0xF

            state = IP, IS, R0, R1, memory
            state = exec_instruction(state)
            IP, IS, R0, R1, memory = state

            cycle += 1

            # Exit the for the HLT instruction
            if IS == 0:
                break

    if debug and not quit:
        visualizer((IP, IS, R0, R1, memory), highlight, cycle)
