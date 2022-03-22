import re
from cpu.instruction_set import mnemonics, InstructionType

REGISTER_PATTERN = re.compile(r"([A-Z]+?)_(R[01])", re.IGNORECASE)


def disassemble(state, highlight, cycle=0):
    IP, IS, R0, R1, memory = state

    print("-" * 23)

    index = 0
    while index < len(memory):

        IS = memory[index]
        mnemonic, type = mnemonics[IS]
        marker = ">" if index == IP else " "

        # if halt_seen:
        #     # memory after HTL assumed to be data
        #     print(f" {index:02d}: {IS:02d}")
        #     index += 1
        if type == InstructionType.STATELESS:
            # no operand
            print(f"{marker}{index:02d}: {IS:02d}     {mnemonic:5}")
            index += 1
        elif type == InstructionType.REGISTER:
            match = REGISTER_PATTERN.match(mnemonic)
            if not match:
                raise Exception("Internal error in disassembler")
            mnemonic = match.group(1)
            register = match.group(2)
            print(f"{marker}{index:02d}: {IS:02d}     {mnemonic:5} {register}")
            index += 1
        elif type == InstructionType.IO:
            if index >= len(memory) - 1:
                # End of memory, no operand: treat as data
                print(f" {index:02d}: {IS:02d}     ???")
                index += 1
            else:
                operand = memory[index + 1]
                print(
                    f"{marker}{index:02d}: {IS:02d} {operand:02}  {mnemonic:5} {operand}"
                )
                index += 2
        elif type == InstructionType.MEMORY:
            if index >= len(memory) - 1:
                # End of memory, no operand: treat as data
                print(f" {index:02d}: {IS:02d}     ???")
                index += 1
            else:
                operand = memory[index + 1]
                match = REGISTER_PATTERN.match(mnemonic)
                if not match:
                    raise Exception("Internal error in disassembler")
                mnemonic = match.group(1)
                register = match.group(2)
                print(
                    f"{marker}{index:02d}: {IS:02d} {operand:02}  {mnemonic:5} {register},{operand}"
                )
                index += 2
        elif type == InstructionType.BRANCH:
            # one operand
            if index >= len(memory) - 1:
                # End of memory, no operand: treat as data
                print(f" {index:02d}: {IS:02d}")
            else:
                operand = memory[index + 1]
                print(
                    f"{marker}{index:02d}: {IS:02d} {operand:02}  {mnemonic:5} {operand}"
                )
                index += 2

        else:
            raise Exception(f"Invalid instruction type: {type}")

    IS = memory[IP]
    mnemonic = mnemonics[IS][0].replace("_", " ")
    print(f"\n IP: {IP}, R0: {R0}, R1: {R1}, IS: {IS} ({mnemonic}), Cycle: {cycle}\n")
