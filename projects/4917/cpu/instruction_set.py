from enum import Enum, auto


class InstructionType(Enum):
    BRANCH = auto()
    MEMORY = auto()
    REGISTER = auto()
    REGISTER_ALIAS = auto()
    STATELESS = auto()


mnemonics = [
    ("HLT", InstructionType.STATELESS),  # 0
    ("ADD", InstructionType.REGISTER),  # 1
    ("SUB", InstructionType.REGISTER),  # 2
    ("INC0", InstructionType.REGISTER),  # 3
    ("INC1", InstructionType.REGISTER),  # 4
    ("DEC0", InstructionType.REGISTER),  # 5
    ("DEC1", InstructionType.REGISTER),  # 6
    ("BEEP", InstructionType.STATELESS),  # 7
    ("PRINT", InstructionType.MEMORY),  # 8
    ("LDR0", InstructionType.MEMORY),  # 9
    ("LDR1", InstructionType.MEMORY),  # 10
    ("STR0", InstructionType.MEMORY),  # 11
    ("STR1", InstructionType.MEMORY),  # 12
    ("B", InstructionType.BRANCH),  # 13
    ("BZ", InstructionType.BRANCH),  # 14
    ("BNZ", InstructionType.BRANCH),  # 15
    ("INC", InstructionType.REGISTER_ALIAS),
    ("DEC", InstructionType.REGISTER_ALIAS),
    ("LD", InstructionType.REGISTER_ALIAS),
    ("ST", InstructionType.REGISTER_ALIAS),
]

def loopup_mnemonic(text):
    try:
        return next(
            (opcode, instr[1])
            for (opcode, instr) in enumerate(mnemonics)
            if instr[0] == text
        )
    except StopIteration:
        return None

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


instruction_set = [
    (HLT, InstructionType.STATELESS),  # 0
    (ADD, InstructionType.REGISTER),  # 1
    (SUB, InstructionType.REGISTER),  # 2
    (INC0, InstructionType.REGISTER),  # 3
    (INC1, InstructionType.REGISTER),  # 4
    (DEC0, InstructionType.REGISTER),  # 5
    (DEC1, InstructionType.REGISTER),  # 6
    (BEEP, InstructionType.STATELESS),  # 7
    (PRINT, InstructionType.MEMORY),  # 8
    (LDR0, InstructionType.MEMORY),  # 9
    (LDR1, InstructionType.MEMORY),  # 10
    (STR0, InstructionType.MEMORY),  # 11
    (STR1, InstructionType.MEMORY),  # 12
    (B, InstructionType.BRANCH),  # 13
    (BZ, InstructionType.BRANCH),  # 14
    (BNZ, InstructionType.BRANCH),  # 15
]
