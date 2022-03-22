import re
from enum import Enum
from sre_parse import WHITESPACE
from tkinter import END

from cpu.instruction_set import InstructionType, instruction_set, mnemonics


class Token(Enum):
    DIRECTIVE = 1
    NAME = 2
    NUMBER = 3
    LOCATION = 4
    COMMENT = 5
    WHITESPACE = 6
    EOL = 7


token_patterns = [
    (Token.DIRECTIVE, re.compile(r"\.([a-z]+)", re.IGNORECASE)),
    (Token.NAME, re.compile(r"([a-z]+\d?)", re.IGNORECASE)),
    (Token.LOCATION, re.compile(r"(\d+):")),
    (Token.NUMBER, re.compile(r"(\d+)")),
    (Token.COMMENT, re.compile(r"(\s*;;)")),
    (Token.WHITESPACE, re.compile(r"(\s+)")),
]


class AsmError(Exception):
    def __init__(self, reason, pos, line):
        pointer = (" " * pos) + "^"
        self.message = f"{reason}:\n{line}\n{pointer}"
        super().__init__(self.message)


def tokenizer(line):
    start = 0
    stop = len(line)
    while start < stop:
        for type, pattern in token_patterns:
            match = pattern.match(line, start)
            if match:
                text = match.group(1).lower()
                yield type, text, start
                start = match.end()
                break
        else:
            raise AsmError("Syntax error", start, line)
    yield Token.EOL, "", 0


END_OF_STATEMENT_TOKENS = Token.COMMENT, Token.EOL


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
        while token not in END_OF_STATEMENT_TOKENS:
            if token == Token.DIRECTIVE:
                if text != "data":
                    raise AsmError("Invalid directive", pos, line)
                data_directive_seen = True
                token, text, pos = next(iter)
                if token == Token.WHITESPACE:
                    token, text, pos = next(iter)
                if token not in END_OF_STATEMENT_TOKENS:
                    raise AsmError("Extra garbage on line", pos, line)
            elif token == Token.NAME:
                if data_directive_seen:
                    raise AsmError(f"Expected a data definition", pos, line)

                # look up the opcode for this mnemonic
                try:
                    opcode = mnemonics.index(text)
                except ValueError:
                    raise AsmError("Invalid mnemonic", pos, line)

                if address >= len(binary_code):
                    raise AsmError("Your program exceeds memory capacity.", pos, line)

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
                    if token not in END_OF_STATEMENT_TOKENS:
                        raise AsmError("Extra garbage on line", pos, line)
                else:
                    # instruction with an operand
                    token, text, pos = next(iter)
                    if token == Token.WHITESPACE:
                        token, text, pos = next(iter)
                    if token != Token.NUMBER:
                        raise AsmError(f"Expected numeric operand", pos, line)
                    if address >= len(binary_code):
                        raise AsmError(
                            "Your program exceeds memory capacity.", pos, line
                        )
                    operand = int(text)
                    if not (0 <= operand < 16):
                        raise AsmError("Operand out of range", pos, line)
                    binary_code[address] = operand
                    address += 1
                    token, text, pos = next(iter)
                    if token not in END_OF_STATEMENT_TOKENS:
                        raise AsmError("Extra garbage on line", pos, line)
            elif token == Token.LOCATION:
                if not data_directive_seen:
                    raise AsmError("Invalid placement", pos, line)
                location = int(text)
                if not (0 <= location < 16):
                    raise AsmError("Address out of range", pos, line)
                token, text, pos = next(iter)
                if token == Token.WHITESPACE:
                    token, text, pos = next(iter)
                if token != Token.NUMBER:
                    raise AsmError("Expected numeric operand", pos, line)
                operand = int(text)
                if not (0 <= operand < 16):
                    raise AsmError("Operand out of range", pos, line)
                binary_code[location] = operand
                token, text, pos = next(iter)
                if token not in END_OF_STATEMENT_TOKENS:
                    raise AsmError("Extra garbage on line", pos, line)
            else:
                raise AsmError("Invalid token", pos, line)

    return binary_code
