import time

from cpu.instruction_set import InstructionType, instruction_set
from cpu.ascii_visualizer import ascii
from cpu.disassembler import disassemble


def exec_instruction(state, instruction):
    IP, R0, R1, memory = state
    microcode, type = instruction

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

    return IP, R0, R1, memory


def cpu(visualize, memory, IP=0, R0=0, R1=0, debug=True):
    cycle = 0
    quit = False
    visualizer = ascii if visualize == "matrix" else disassemble
    visualizer_toggled = False

    while True:
        # Fetch the next instruction
        IS = memory[IP]

        highlight = [IP]
        if IS >= 8:
            highlight = [IP, (IP + 1) & 0xF]

        if debug:
            visualizer = ascii if visualize == "matrix" else disassemble
            visualizer((IP, IS, R0, R1, memory), highlight, cycle)
            inp = input("hit enter to continue or 'q' enter to quit> ")
            if inp == "q":
                quit = True
                break
            elif inp == "t":
                # toggle visualizer
                visualize = "asm" if visualize == "matrix" else "matrix"
                visualizer_toggled = True
            else:
                print()
        else:
            time.sleep(0.1)

        if visualizer_toggled:
            visualizer_toggled = False
        else:
            # Increment the instruction pointer
            IP = (IP + 1) & 0xF

            # Lookup the function to execute and the width of the instruction
            instruction = instruction_set[IS]

            state = IP, R0, R1, memory
            state = exec_instruction(state, instruction)
            IP, R0, R1, memory = state

            cycle += 1

            # Exit the for the HLT instruction
            if IS == 0:
                break

    if debug and not quit:
        visualizer((IP, IS, R0, R1, memory), highlight, cycle)
