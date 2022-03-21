import re
from enum import Enum

from cpu.instruction_set import InstructionType, instruction_set, mnemonics


class TokenType(Enum):
    DIRECTIVE = 1
    NAME = 2
    NUMBER = 3
    LOCATION = 4
    COMMENT = 5
    EOL = 6


token_patterns = [
    (TokenType.DIRECTIVE, re.compile(r"\s*\.([A-Z]+)")),
    (TokenType.NAME, re.compile(r"\s*([A-Z]+\d?)")),
    (TokenType.LOCATION, re.compile(r"\s*(\d+):")),
    (TokenType.NUMBER, re.compile(r"\s*(\d+)")),
    (TokenType.COMMENT, re.compile(r"\s*(;;)")),
]


class AsmException(Exception):
    def __init__(self, reason, pos, line):
        super().__init__(f"{reason} at position {pos}:\n{line}")


def tokenizer(line):
    start = 0
    stop = len(line)
    while start < stop:
        for type, pattern in token_patterns:
            match = pattern.match(line, start)
            if match:
                text = match.group(1).upper()
                yield type, text, start
                start = match.end()
                break
        else:
            raise AsmException("Syntax error", start, line)
    yield TokenType.EOL, "", 0


def assemble(file):
    # zero fill the binary code to size of the machine memory
    binary_code = [0] * 16
    address = 0

    data_directive_seen = False

    for line in file:
        line = line.strip()

        # skip blank lines
        if not line:
            continue

        iter = tokenizer(line)

        token, text, pos = next(iter)
        while token != TokenType.EOL:
            if token == TokenType.COMMENT:
                break
            elif token == TokenType.DIRECTIVE:
                if text != "DATA":
                    raise AsmException("Invalid directive", pos, line)
                data_directive_seen = True
                token, text, pos = next(iter)
            elif token == TokenType.NAME:
                if data_directive_seen:
                    raise AsmException(f"Invalid data definition", pos, line)

                # look up the opcode for this mnemonic
                try:
                    opcode = mnemonics.index(text)
                except ValueError:
                    raise AsmException("Invalid mnemonic", pos, line)

                if address >= len(binary_code):
                    raise AsmException(
                        "Your program exceeds memory capacity.", pos, line
                    )

                # add the opcode the to binary output
                binary_code[address] = opcode
                address += 1

                # look up the instruction type
                microcode, instruction_type = instruction_set[opcode]

                if (
                    instruction_type == InstructionType.REGISTER
                    or instruction_type == InstructionType.STATELESS
                ):
                    # instructions without an operand
                    token, text, pos = next(iter)
                    if token != TokenType.COMMENT and token != TokenType.EOL:
                        raise AsmException("Extra garbage on line", pos, line)
                else:
                    # instruction with an operand
                    token, text, pos = next(iter)
                    if token != TokenType.NUMBER:
                        raise AsmException(f"Expected numeric operand", pos, line)
                    if address >= len(binary_code):
                        raise AsmException(
                            "Your program exceeds memory capacity.", pos, line
                        )
                    operand = int(text)
                    if not (0 <= operand < 16):
                        raise Exception("Operand out of range", pos, line)
                    binary_code[address] = operand
                    address += 1
                    token, text, pos = next(iter)
            elif token == TokenType.LOCATION:
                if not data_directive_seen:
                    raise AsmException("Invalid placement", pos, line)
                location = int(text)
                if not (0 <= location < 16):
                    raise AsmException("Address out of range", pos, line)
                token, text, pos = next(iter)
                if token != TokenType.NUMBER:
                    raise AsmException("Expected numeric operand", pos, line)
                operand = int(text)
                if not (0 <= operand < 16):
                    raise AsmException("Operand out of range", pos, line)
                binary_code[location] = operand
                token, text, pos = next(iter)

            else:
                raise AsmException("Invalid token", pos, line)

    return binary_code
