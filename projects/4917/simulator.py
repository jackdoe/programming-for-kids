import sys

mnemonics = [
    "HLT",  # 0
    "ADD",  # 1
    "SUB",  # 2
    "INC0",  # 3
    "INC1",  # 4
    "DEC0",  # 5
    "DEC1",  # 6
    "BEEP",  # 7
    "PRINT",  # 8
    "LDR0",  # 9
    "LDR1",  # 10
    "STR0",  # 11
    "STR1",  # 12
    "B",  # 13
    "BZ",  # 14
    "BNZ",  # 15
]


def HLT():
    print("\n*** HALT ***")


def ADD(R0, R1):
    R0 += R1
    return R0, R1


def SUB(R0, R1):
    R0 -= R1
    return R0, R1


def INC0(R0, R1):
    R0 += 1
    return R0, R1


def INC1(R0, R1):
    R1 += 1
    return R0, R1


def DEC0(R0, R1):
    R0 -= 1
    return R0, R1


def DEC1(R0, R1):
    R1 -= 1
    return R0, R1


def BEEP():
    print("\n*** BEEP ***")


def PRINT(R0, R1, IP, memory):
    print("\n***", memory[memory[IP]], "***")
    return R0, R1, memory


def LDR0(R0, R1, IP, memory):
    R0 = memory[memory[IP]]
    return R0, R1, memory


def LDR1(R0, R1, IP, memory):
    R1 = memory[memory[IP]]
    return R0, R1, memory


def STR0(R0, R1, IP, memory):
    memory[memory[IP]] = R0
    return R0, R1, memory


def STR1(R0, R1, IP, memory):
    memory[memory[IP]] = R1
    return R0, R1, memory


def B(IP, R0, memory):
    IP = memory[IP]
    return IP


def BZ(IP, R0, memory):
    if R0 == 0:
        IP = memory[IP]
    else:
        IP += 1
    return IP


def BNZ(IP, R0, memory):
    if R0 != 0:
        IP = memory[IP]
    else:
        IP += 1
    return IP


# [microcode, type: 1 = register, 2 = memory, 3 = branch, 4 = stateless]
instruction_set = [
    [HLT, 4],  # 0
    [ADD, 1],  # 1
    [SUB, 1],  # 2
    [INC0, 1],  # 3
    [INC1, 1],  # 4
    [DEC0, 1],  # 5
    [DEC1, 1],  # 6
    [BEEP, 4],  # 7
    [PRINT, 2],  # 8
    [LDR0, 2],  # 9
    [LDR1, 2],  # 10
    [STR0, 2],  # 11
    [STR1, 2],  # 12
    [B, 3],  # 13
    [BZ, 3],  # 14
    [BNZ, 3],  # 15
]


def disassemble(state):
    IP, IS, R0, R1, memory = state

    print(f"\n IP: {IP}, IS: {IS}, R0: {R0}, R1: {R1}\n")

    index = 0
    halt_seen = False
    while index < len(memory):
        IS = memory[index]
        microcode, type = instruction_set[IS]
        mnemonic = mnemonics[IS]
        marker = ">" if index == IP else " "

        if halt_seen:
            # memory after HTL assumed to be data
            print(f" {index:02d}: {IS:02d}")
            index += 1
        elif type == 1 or type == 4:
            # register instruction
            print(f"{marker}{index:02d}: {IS:02d}     {mnemonic:5}")
            index += 1
        elif type == 2 or type == 3:
            # memory instruction
            operand = memory[index + 1]
            print(
                f"{marker}{index:02d}: {IS:02d} {operand:02d}  {mnemonic:5} {operand}"
            )
            index += 2
        else:
            raise Exception(f"Invalid instruction type: ${type}")

        if IS == 0:
            halt_seen = True


def exec_instruction(state, instruction):
    IP, R0, R1, memory = state
    microcode, type = instruction

    if type == 1:
        # register instruction
        R0, R1 = microcode(R0, R1)
    elif type == 2:
        # memory instruction
        R0, R1, memory = microcode(R0, R1, IP, memory)
        IP += 1
    elif type == 3:
        # branch instruction
        IP = microcode(IP, R0, memory)
    elif type == 4:
        # stateless instruction
        microcode()
    else:
        raise Exception(f"Invalid instruction type {type}")

    # truncate registers to 4 bits (all are unsigned nibbles)
    IP, R0, R1 = (register & 0xF for register in (IP, R0, R1))

    return IP, R0, R1, memory


def cpu(IP, R0, R1, memory, debug=True):
    IS = 0

    while True:
        if debug:
            disassemble((IP, IS, R0, R1, memory))
            input("hit enter to continue> ")

        # Fetch the next instruction
        IS = memory[IP]

        # Increment the instruction pointer
        IP = (IP + 1) & 0xF

        # Lookup the function to execute and the width of the instruction
        instruction = instruction_set[IS]

        state = IP, R0, R1, memory
        state = exec_instruction(state, instruction)
        IP, R0, R1, memory = state

        # Exit the for the HLT instruction
        if IS == 0:
            break

    if debug:
        disassemble((IP, IS, R0, R1, memory))


def load_matrix():
    if len(sys.argv) == 1 or ".prg" not in sys.argv[1]:
        print("usage: python3 ", sys.argv[0] + " file.prg")
        sys.exit(1)

    f = open(sys.argv[1])

    # for running the debugger
    # f = open(r".\projects\4917\deck\01.prg")

    state = []
    for line in f.readlines():
        if "#" in line:
            continue
        line = line.replace("│", " ")
        line = line.replace("_", " ")
        row = []
        for s in line.split():
            if s.isdigit():
                row.append(int(s))
        # remove first and last element in case its pasted from our output
        if len(row) == 6:
            row.pop(5)
            row.pop(0)
        if len(row) > 0:
            state += row
    f.close()
    return state


if __name__ == "__main__":
    IP, IS, RO, R1, *memory = load_matrix()

    # Note: IS is not part of the state. It is an internal CPU register
    # not externally accessible
    cpu(IP, RO, R1, memory)
