import re
from cpu.instruction_set import mnemonics, InstructionType

REGISTER_PATTERN = re.compile(r"([A-Z]+?)_(R[01])", re.IGNORECASE)


def is_ip_aligned(IP, memory):
    index = 0
    ip_aligned = False
    while index < len(memory):
        IS = memory[index]
        mnemonic, type = mnemonics[IS]
        if type == InstructionType.STATELESS:
            index += 1
        elif type == InstructionType.REGISTER:
            index += 1
        elif type == InstructionType.IO:
            index += 2
        elif type == InstructionType.MEMORY:
            index += 2
        elif type == InstructionType.BRANCH:
            index += 2
        if IP == index:
            ip_aligned = True
    return ip_aligned


def get_new_start(IP, memory):
    index = IP
    prev_index = index
    while index > 0:
        prev_index = index
        IS = memory[index]
        mnemonic, type = mnemonics[IS]
        if type == InstructionType.STATELESS:
            index -= 1
        elif type == InstructionType.REGISTER:
            index -= 1
        elif type == InstructionType.IO:
            index -= 2
        elif type == InstructionType.MEMORY:
            index -= 2
        elif type == InstructionType.BRANCH:
            index -= 2
    return prev_index


def disassemble(state, highlight, cycle=0):
    IP, IS, R0, R1, memory = state

    count = 0
    address = 0 if is_ip_aligned(IP, memory) else IP

    # if count != address:
    #     print("new_start", get_new_start(IP, memory))

    print("-" * 23)

    while count < len(memory):
        IS = memory[address]
        mnemonic, type = mnemonics[IS]
        marker = ">" if address == IP else " "

        if type == InstructionType.STATELESS:
            # no operand
            print(f"{marker}{address:02d}: {IS:02d}     {mnemonic:5}")
            address += 1
            count += 1
        elif type == InstructionType.REGISTER:
            match = REGISTER_PATTERN.match(mnemonic)
            if not match:
                raise Exception("Internal error in disassembler")
            mnemonic = match.group(1)
            register = match.group(2)
            print(f"{marker}{address:02d}: {IS:02d}     {mnemonic:5} {register}")
            address += 1
            count += 1
        elif type == InstructionType.IO:
            if count >= len(memory) - 1:
                # End of memory, no operand: treat as data
                print(f" {address:02d}: {IS:02d}     ???")
                address += 1
                count += 1
            else:
                operand = memory[address + 1]
                print(
                    f"{marker}{address:02d}: {IS:02d} {operand:02}  {mnemonic:5} {operand}"
                )
                address += 2
                count += 2
        elif type == InstructionType.MEMORY:
            if count >= len(memory) - 1:
                # End of memory, no operand: treat as data
                print(f" {address:02d}: {IS:02d}     ???")
                address += 1
                count += 2
            else:
                operand = memory[address + 1]
                match = REGISTER_PATTERN.match(mnemonic)
                if not match:
                    raise Exception("Internal error in disassembler")
                mnemonic = match.group(1)
                register = match.group(2)
                print(
                    f"{marker}{address:02d}: {IS:02d} {operand:02}  {mnemonic:5} {register},{operand}"
                )
                address += 2
                count += 2
        elif type == InstructionType.BRANCH:
            # one operand
            if count >= len(memory) - 1:
                # End of memory, no operand: treat as data
                print(f" {address:02d}: {IS:02d}     ???")
                address += 1
                count += 1
            else:
                operand = memory[address + 1]
                print(
                    f"{marker}{address:02d}: {IS:02d} {operand:02}  {mnemonic:5} {operand}"
                )
                address += 2
                count += 2

        else:
            raise Exception(f"Invalid instruction type: {type}")

        address &= 0xF

    print(f"\n R0: {R0}, R1: {R1}, Cycle: {cycle}\n")
