import re
from enum import Enum, auto

from cpu.instruction_set import InstructionType, loopup_mnemonic, mnemonics

BAD_DIRECTIVE = "Invalid directive"
BAD_MNEMONIC = "Invalid mnemonic"
BAD_OPERAND = "Operand is invalid"
BAD_REGISTER = "Invalid register"
COMMA_EXPECTED = "Expected a ','"
EXTRA_GARBAGE = "Extra garbage on line"
NUMBER_EXPECTED = "Expected a number"
OUT_OF_RANGE = "Number is out of range"
STORE_OVERFLOW = "Program exceeds available memory"
SYNTAX_ERROR = "Syntax error"
UNDEFINED_OPERAND = "Operand is undefined"


class Token(Enum):
    COMMA = auto()
    COMMENT = auto()
    DIRECTIVE = auto()
    EOL = auto()
    LABEL = auto()
    LOCATION = auto()
    MINUS = ()
    NAME = auto()
    NUMBER = auto()
    PLUS = ()
    REGISTER = auto()
    WHITESPACE = auto()


token_patterns = [
    (Token.DIRECTIVE, re.compile(r"\.([A-Z]+)", re.IGNORECASE)),
    (Token.LABEL, re.compile(r"([A-Z]\w*):", re.IGNORECASE)),
    (Token.REGISTER, re.compile(r"(R[01])", re.IGNORECASE)),
    (Token.NAME, re.compile(r"([A-Z]\w*)", re.IGNORECASE)),
    (Token.LOCATION, re.compile(r"(\d+):")),
    (Token.NUMBER, re.compile(r"(\d+)")),
    (Token.COMMA, re.compile(r"(,)")),
    (Token.PLUS, re.compile(r"(\+)")),
    (Token.MINUS, re.compile(r"(-)")),
    (Token.COMMENT, re.compile(r"(\s*;)")),
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
            raise AsmError(SYNTAX_ERROR, start, line)
    yield Token.EOL, "", 0


END_OF_STATEMENT_TOKENS = Token.COMMENT, Token.EOL


def check_store(address, store, pos, line):
    if address >= len(store):
        raise AsmError(STORE_OVERFLOW, pos, line)


def check_number(number, pos, line):
    if not (0 <= number < 16):
        raise AsmError(OUT_OF_RANGE, pos, line)
    return number


def assemble(file):
    # zero fill the binary code to size of the machine memory
    store = [0] * 16
    symbol_table = dict()

    for _pass in range(1, 3):
        file.seek(0)
        address = 0

        for line in file:
            line = line.strip()

            # skip blank lines
            if not line:
                continue

            iter = tokenizer(line)

            token, text, pos = next(iter)
            while token not in END_OF_STATEMENT_TOKENS:
                if token == Token.LABEL:
                    if _pass == 1:
                        symbol_table[text] = address
                    token, text, pos = next(iter)
                    if token == Token.WHITESPACE:
                        token, text, pos = next(iter)
                    if token in END_OF_STATEMENT_TOKENS:
                        break
                if token == Token.DIRECTIVE:
                    if text != "DATA":
                        raise AsmError(BAD_DIRECTIVE, pos, line)
                    token, text, pos = next(iter)
                    if token == Token.WHITESPACE:
                        token, text, pos = next(iter)
                    if token != Token.NUMBER:
                        raise AsmError(NUMBER_EXPECTED, pos, line)
                    operand = check_number(int(text), pos, line)
                    if _pass == 2:
                        check_store(address, store, pos, line)
                        store[address] = operand
                    address += 1
                    token, text, pos = next(iter)
                    if token is Token.WHITESPACE:
                        token, text, pos = next(iter)
                    if token not in END_OF_STATEMENT_TOKENS:
                        raise AsmError(EXTRA_GARBAGE, pos, line)
                elif token == Token.NAME:

                    mnemonic = text

                    # look up the opcode for this mnemonic
                    found = loopup_mnemonic(text)
                    if not found:
                        raise AsmError(BAD_MNEMONIC, pos, line)
                    opcode, instruction_type = found

                    token, text, pos = next(iter)

                    if instruction_type in (
                        InstructionType.REGISTER_ALIAS_1,
                        InstructionType.REGISTER_ALIAS_2,
                    ):
                        if token == Token.WHITESPACE:
                            token, text, pos = next(iter)
                        if token != Token.REGISTER:
                            raise AsmError(BAD_REGISTER, pos, line)
                        mnemonic += f"_{text}"

                        token, text, pos = next(iter)
                        if token == Token.WHITESPACE:
                            token, text, pos = next(iter)

                        if instruction_type is InstructionType.REGISTER_ALIAS_2:
                            # takes a second operand
                            if token != Token.COMMA:
                                raise AsmError(COMMA_EXPECTED, pos, line)
                            token, text, pos = next(iter)

                        # look up the opcode for the modified mnemonic
                        found = loopup_mnemonic(mnemonic)
                        if not found:
                            raise AsmError(BAD_MNEMONIC, pos, line)
                        opcode, instruction_type = found

                    # add the opcode the to binary output
                    if _pass == 2:
                        check_store(address, store, pos, line)
                        store[address] = opcode
                    address += 1

                    if instruction_type in (
                        InstructionType.REGISTER,
                        InstructionType.REGISTER_ALIAS_1,
                        InstructionType.STATELESS,
                    ):
                        # instructions without an operand
                        if token not in END_OF_STATEMENT_TOKENS:
                            raise AsmError(EXTRA_GARBAGE, pos, line)
                    else:
                        # instruction with an operand
                        operand = 0
                        if token == Token.WHITESPACE:
                            token, text, pos = next(iter)
                        if token == Token.NUMBER:
                            operand = int(text)
                        elif token == Token.NAME:
                            if _pass == 2:
                                if text not in symbol_table:
                                    raise AsmError(UNDEFINED_OPERAND, pos, line)
                                operand = symbol_table[text]
                        else:
                            raise AsmError(BAD_OPERAND, pos, line)
                        token, text, pos = next(iter)
                        # check of offset
                        if token in (Token.PLUS, Token.MINUS):
                            operator_text = text
                            token, text, pos = next(iter)
                            if token == Token.WHITESPACE:
                                token, text, pos = next(iter)
                            if token != Token.NUMBER:
                                raise AsmError(NUMBER_EXPECTED, pos, line)
                            offset = check_number(int(text), pos, line)
                            if operator_text == "+":
                                operand += offset
                            else:
                                operand -= offset
                            operand &= 0xF
                            token, text, pos = next(iter)
                            if token is Token.WHITESPACE:
                                token, text, pos = next(iter)
                        check_number(operand, pos, line)
                        if _pass == 2:
                            check_store(address, store, pos, line)
                            store[address] = operand
                        address += 1
                        if token not in END_OF_STATEMENT_TOKENS:
                            raise AsmError(EXTRA_GARBAGE, pos, line)
                else:
                    raise AsmError(SYNTAX_ERROR, pos, line)

    return store
