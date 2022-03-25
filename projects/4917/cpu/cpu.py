from sre_constants import IN
import time
from enum import Enum, auto

from cpu.instruction_set import InstructionType, instruction_set
from cpu.ascii_visualizer import ascii
from cpu.disassembler import disassemble
from cpu.debug_menu import debug_more_menu


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
            inp = input("Hit enter to continue, 'm' for more or 'q' to quit> ")
            if inp == "q":
                quit = True
                break
            elif inp == "m":
                IP, R0, R1, memory, visualize = debug_more_menu(
                    IP, R0, R1, memory, visualize
                )
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
