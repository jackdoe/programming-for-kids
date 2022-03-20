from dis import dis
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


def overflow_add(x, n):
    return (x + n) & 0xF


def HLT(IP, R0, R1, memory):
    print("\n*** HALT ***")
    return IP, R0, R1, memory


def ADD(IP, R0, R1, memory):
    R0 += R1
    return IP, R0, R1, memory


def SUB(IP, R0, R1, memory):
    R0 -= R1
    return IP, R0, R1, memory


def INC0(IP, R0, R1, memory):
    R0 += 1
    return IP, R0, R1, memory


def INC1(IP, R0, R1, memory):
    R1 += 1
    return IP, R0, R1, memory


def DEC0(IP, R0, R1, memory):
    R0 -= 1
    return IP, R0, R1, memory


def DEC1(IP, R0, R1, memory):
    R1 -= 1
    return IP, R0, R1, memory


def BEEP(IP, R0, R1, memory):
    print("\n*** BEEP ***")
    return IP, R0, R1, memory


def PRINT(IP, R0, R1, memory):
    print("\n*** ", memory[IP], "***")
    IP = overflow_add(IP, 1)
    return IP, R0, R1, memory


def LDR0(IP, R0, R1, memory):
    R0 = memory[memory[IP]]
    IP = overflow_add(IP, 1)
    return IP, R0, R1, memory


def LDR1(IP, R0, R1, memory):
    R1 = memory[memory[IP]]
    IP = overflow_add(IP, 1)
    return IP, R0, R1, memory


def STR0(IP, R0, R1, memory):
    memory[memory[IP]] = R0
    IP = overflow_add(IP, 1)
    return IP, R0, R1, memory


def STR1(IP, R0, R1, memory):
    memory[memory[IP]] = R1
    IP = overflow_add(IP, 1)
    return IP, R0, R1, memory


def B(IP, R0, R1, memory):
    IP = memory[IP]
    IP = overflow_add(IP, 1)
    return IP, R0, R1, memory


def BZ(IP, R0, R1, memory):
    IP = memory[IP] if R0 == 0 else overflow_add(IP, 1)
    return IP, R0, R1, memory


def BNZ(IP, R0, R1, memory):
    IP = memory[IP] if R0 != 0 else overflow_add(IP, 1)
    return IP, R0, R1, memory


# [function, instruction width]
instruction_set = [
    [HLT, 1],  # 0
    [ADD, 1],  # 1
    [SUB, 1],  # 2
    [INC0, 1],  # 3
    [INC1, 1],  # 4
    [DEC0, 1],  # 5
    [DEC1, 1],  # 6
    [BEEP, 1],  # 7
    [PRINT, 2],  # 8
    [LDR0, 2],  # 9
    [LDR1, 2],  # 10
    [STR0, 2],  # 11
    [STR1, 2],  # 12
    [B, 2],  # 13
    [BZ, 2],  # 14
    [BNZ, 2],  # 15
]


def disassemble(state):
    IP, IS, R0, R1, memory = state

    print(f"\nIP: {IP}, IS: {IS}, R0: {R0}, R1: {R1}")

    index = 0
    halt_seen = False
    while index < len(memory):
        IS = memory[index]
        microcode, width = instruction_set[IS]
        mnemonic = mnemonics[IS]
        marker = ">" if index == IP else " "

        if halt_seen:
            print(f" {index:02d}: {IS}")
        elif width == 1:
            print(f"{marker}{index:02d}: {mnemonic:5}")
        else:
            print(f"{marker}{index:02d}: {mnemonic:5} {memory[index+1]}")

        index += width

        if IS == 0:
            halt_seen = True


def cpu(IP, IS, R0, R1, memory, debug=True):
    while True:
        if debug:
            disassemble((IP, IS, R0, R1, memory))
            input("hit enter to continue> ")

        # Fetch the next instruction
        IS = memory[IP]

        # Increment the instruction pointer
        IP = overflow_add(IP, 1)

        # Lookup the function to execute and the width of the instruction
        microcode, width = instruction_set[IS]

        # Execute the instruction code
        IP, R0, R1, memory = microcode(IP, R0, R1, memory)

        # Exit the for the HLT instruction
        if IS == 0:
            break

    if debug:
        disassemble((IP, IS, R0, R1, memory))


def load_program():
    if len(sys.argv) == 1 or ".prg" not in sys.argv[1]:
        print("usage: python3 ", sys.argv[0] + " file.prg")
        sys.exit(1)

    f = open(sys.argv[1])
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
    IP, IS, RO, R1, *memory = load_program()

    # Note: IS is not part of the state. It is an internal CPU register
    # not externally accessible
    cpu(IP, IS, RO, R1, memory)
