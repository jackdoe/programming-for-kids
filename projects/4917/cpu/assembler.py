import re
from enum import Enum, auto

from cpu.instruction_set import InstructionType, mnemonics, loopup_mnemonic


class Token(Enum):
    COMMA = auto()
    COMMENT = auto()
    DIRECTIVE = auto()
    EOL = auto()
    LOCATION = auto()
    NAME = auto()
    NUMBER = auto()
    REGISTER = auto()
    WHITESPACE = auto()


token_patterns = [
    (Token.DIRECTIVE, re.compile(r"\.([A-Z]+)", re.IGNORECASE)),
    (Token.REGISTER, re.compile(r"(R[01])", re.IGNORECASE)),
    (Token.NAME, re.compile(r"([A-Z]+\d?)", re.IGNORECASE)),
    (Token.LOCATION, re.compile(r"(\d+):")),
    (Token.NUMBER, re.compile(r"(\d+)")),
    (Token.COMMA, re.compile(r"(,)")),
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
                text = match.group(1).upper()
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
                if text != "DATA":
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

                mnemonic = text

                # look up the opcode for this mnemonic
                found = loopup_mnemonic(text)
                if not found:
                    raise AsmError("Invalid mnemonic", pos, line)
                opcode, instruction_type = found

                if instruction_type == InstructionType.REGISTER_ALIAS:
                    token, text, pos = next(iter)
                    if token == Token.WHITESPACE:
                        token, text, pos = next(iter)
                    if token != Token.REGISTER:
                        raise AsmError("Expected R0 or R1", pos, line)
                    mnemonic += text

                    # look up the opcode for the modified mnemonic
                    found = loopup_mnemonic(mnemonic)
                    if not found:
                        raise AsmError("Invalid mnemonic", pos, line)
                    opcode, instruction_type = found

                    token, text, pos = next(iter)
                    if token == Token.WHITESPACE:
                        token, text, pos = next(iter)

                    if token != Token.COMMA:
                        raise AsmError("Expected a ','", pos, line)

                token, text, pos = next(iter)

                if address >= len(binary_code):
                    raise AsmError("Your program exceeds available memory.", pos, line)

                # add the opcode the to binary output
                binary_code[address] = opcode
                address += 1

                if instruction_type in (
                    InstructionType.REGISTER,
                    InstructionType.STATELESS,
                ):
                    # instructions without an operand
                    if token not in END_OF_STATEMENT_TOKENS:
                        raise AsmError("Extra garbage on line", pos, line)
                else:
                    # instruction with an operand
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
