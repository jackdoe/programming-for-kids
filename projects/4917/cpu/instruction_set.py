from enum import Enum, auto


class InstructionType(Enum):
    BRANCH = auto()
    IO = auto()
    MEMORY = auto()
    REGISTER = auto()
    REGISTER_ALIAS_1 = auto()  # single operand, e.g. R0
    REGISTER_ALIAS_2 = auto()  # two operands, e.g. R0,5
    STATELESS = auto()


mnemonics = [
    ("HLT", InstructionType.STATELESS),  # 0
    ("ADD", InstructionType.STATELESS),  # 1
    ("SUB", InstructionType.STATELESS),  # 2
    ("INC_R0", InstructionType.REGISTER),  # 3
    ("INC_R1", InstructionType.REGISTER),  # 4
    ("DEC_R0", InstructionType.REGISTER),  # 5
    ("DEC_R1", InstructionType.REGISTER),  # 6
    ("BEEP", InstructionType.STATELESS),  # 7
    ("PRINT", InstructionType.IO),  # 8
    ("LD_R0", InstructionType.MEMORY),  # 9
    ("LD_R1", InstructionType.MEMORY),  # 10
    ("ST_R0", InstructionType.MEMORY),  # 11
    ("ST_R1", InstructionType.MEMORY),  # 12
    ("B", InstructionType.BRANCH),  # 13
    ("BZ", InstructionType.BRANCH),  # 14
    ("BNZ", InstructionType.BRANCH),  # 15
    ("INC", InstructionType.REGISTER_ALIAS_1),
    ("DEC", InstructionType.REGISTER_ALIAS_1),
    ("LD", InstructionType.REGISTER_ALIAS_2),
    ("ST", InstructionType.REGISTER_ALIAS_2),
]


def lookup_mnemonic(text):
    try:
        return next(
            (opcode, instr[1])
            for (opcode, instr) in enumerate(mnemonics)
            if instr[0] == text
        )
    except StopIteration:
        return None


def HLT():
    print("*** HALT ***")


def ADD(R0, R1):
    R0 += R1
    return R0, R1


def SUB(R0, R1):
    R0 -= R1
    return R0, R1


def INC_R0(R0, R1):
    R0 += 1
    return R0, R1


def INC_R1(R0, R1):
    R1 += 1
    return R0, R1


def DEC_R0(R0, R1):
    R0 -= 1
    return R0, R1


def DEC_R1(R0, R1):
    R1 -= 1
    return R0, R1


def BEEP():
    print("*** BEEP ***\n")


def PRINT(R0, R1, IP, memory):
    print("***", memory[IP], "***\n")
    return R0, R1, memory


def LD_R0(R0, R1, IP, memory):
    R0 = memory[memory[IP]]
    return R0, R1, memory


def LD_R1(R0, R1, IP, memory):
    R1 = memory[memory[IP]]
    return R0, R1, memory


def ST_R0(R0, R1, IP, memory):
    memory[memory[IP]] = R0
    return R0, R1, memory


def ST_R1(R0, R1, IP, memory):
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
    (INC_R0, InstructionType.REGISTER),  # 3
    (INC_R1, InstructionType.REGISTER),  # 4
    (DEC_R0, InstructionType.REGISTER),  # 5
    (DEC_R1, InstructionType.REGISTER),  # 6
    (BEEP, InstructionType.STATELESS),  # 7
    (PRINT, InstructionType.MEMORY),  # 8
    (LD_R0, InstructionType.MEMORY),  # 9
    (LD_R1, InstructionType.MEMORY),  # 10
    (ST_R0, InstructionType.MEMORY),  # 11
    (ST_R1, InstructionType.MEMORY),  # 12
    (B, InstructionType.BRANCH),  # 13
    (BZ, InstructionType.BRANCH),  # 14
    (BNZ, InstructionType.BRANCH),  # 15
]
