from re import M
from cpu.instruction_set import mnemonics, instruction_set, InstructionType


def disassemble(state, highlight):
    IP, IS, R0, R1, memory = state

    print(f"\n IP: {IP}, IS: {IS}, R0: {R0}, R1: {R1}\n")

    index = 0
    halt_seen = False
    while index < len(memory):
        IS = memory[index]
        microcode, type = instruction_set[IS]
        mnemonic = mnemonics[IS][0]
        marker = ">" if index == IP else " "

        # if halt_seen:
        #     # memory after HTL assumed to be data
        #     print(f" {index:02d}: {IS:02d}")
        #     index += 1
        if type in (InstructionType.REGISTER, InstructionType.STATELESS):
            # no operand
            print(f"{marker}{index:02d}: {IS:02d}     {mnemonic:5}")
            index += 1
        elif type in (InstructionType.MEMORY, InstructionType.BRANCH):
            # one operand
            index += 1
            if index >= len(memory):
                # End of memory, no operand: treat as data
                print(f" {index:02d}: {IS:02d}")
            else:
                operand = memory[index]
                print(
                    f"{marker}{index:02d}: {IS:02d} {operand:02d}  {mnemonic:5} {operand}"
                )
                index += 1
        else:
            raise Exception(f"Invalid instruction type: {type}")

        if IS == 0:
            halt_seen = True

    input("hit enter to continue> ")
