import re
from cpu.instruction_set import mnemonics, InstructionType

REGISTER_PATTERN = re.compile(r"([A-Z]+?)_(R[01])", re.IGNORECASE)


def disassemble(state, highlight, cycle=0):
    IP, IS, R0, R1, memory = state

    print("-" * 23)

    address = 0

    while address < len(memory):
        opcode = memory[address]
        mnemonic, type = mnemonics[opcode]
        marker = ">" if address == IP else " "

        if type == InstructionType.STATELESS:
            # no operand
            print(f"{marker}{address:02d}: {opcode:02d}     {mnemonic:5}")
            address += 1
        elif type == InstructionType.REGISTER:
            match = REGISTER_PATTERN.match(mnemonic)
            if not match:
                raise Exception("Internal error in disassembler")
            mnemonic = match.group(1)
            register = match.group(2)
            print(f"{marker}{address:02d}: {opcode:02d}     {mnemonic:5} {register}")
            address += 1
        elif type == InstructionType.IO:
            if address >= len(memory) - 1 or address == IP - 1:
                # End of memory, no operand: treat as data
                print(f" {address:02d}: {opcode:02d}     ???")
                address += 1
            else:
                operand = memory[address + 1]
                print(
                    f"{marker}{address:02d}: {opcode:02d} {operand:02}  {mnemonic:5} {operand}"
                )
                address += 2
        elif type == InstructionType.MEMORY:
            if address >= len(memory) - 1 or address == IP - 1:
                # End of memory, no operand: treat as data
                print(f" {address:02d}: {opcode:02d}     ???")
                address += 1
            else:
                operand = memory[address + 1]
                match = REGISTER_PATTERN.match(mnemonic)
                if not match:
                    raise Exception("Internal error in disassembler")
                mnemonic = match.group(1)
                register = match.group(2)
                print(
                    f"{marker}{address:02d}: {opcode:02d} {operand:02}  {mnemonic:5} {register},{operand}"
                )
                address += 2
        elif type == InstructionType.BRANCH:
            # one operand
            if address >= len(memory) - 1 or address == IP - 1:
                # End of memory, no operand: treat as data
                print(f" {address:02d}: {opcode:02d}     ???")
                address += 1
            else:
                operand = memory[address + 1]
                print(
                    f"{marker}{address:02d}: {opcode:02d} {operand:02}  {mnemonic:5} {operand}"
                )
                address += 2

        else:
            raise Exception(f"Invalid instruction type: {type}")

    print(f"\nIP: {IP}, IS: {IS}, R0: {R0}, R1: {R1}, Cycle: {cycle}\n")
