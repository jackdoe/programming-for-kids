from cpu.instruction_set import InstructionType, lookup_mnemonic
from cpu.tokenizer import TokenType, tokenizer

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


class AsmError(Exception):
    def __init__(self, reason, pos, line):
        pointer = (" " * pos) + "^"
        self.message = f"{reason}:\n{line}\n{pointer}"
        super().__init__(self.message)


END_OF_STATEMENT_TOKENS = TokenType.COMMENT, TokenType.EOL


def check_store(address, store, pos, line):
    if address >= len(store):
        raise AsmError(STORE_OVERFLOW, pos, line)


def check_number(number, pos, line):
    if not (0 <= number < 16):
        raise AsmError(OUT_OF_RANGE, pos, line)
    return number


INSTRUCTION_ALIASES = (
    InstructionType.REGISTER_ALIAS_1,
    InstructionType.REGISTER_ALIAS_2,
)

SINGLE_NIBBLE_INSTRUCTIONS = (
    InstructionType.REGISTER,
    InstructionType.REGISTER_ALIAS_1,
    InstructionType.STATELESS,
)


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

            token = next(iter)
            while token.type not in END_OF_STATEMENT_TOKENS:
                if token.type is TokenType.LABEL:
                    if _pass == 1:
                        symbol_table[token.text] = address
                    token = next(iter)
                    if token.type in END_OF_STATEMENT_TOKENS:
                        break
                if token.type is TokenType.DIRECTIVE:
                    if token.text != "DATA":
                        raise AsmError(BAD_DIRECTIVE, token.pos, line)
                    operand = 0
                    token = next(iter)
                    if token.type is TokenType.NAME:
                        if _pass == 2:
                            if token.text not in symbol_table:
                                raise AsmError(UNDEFINED_OPERAND, token.pos, line)
                            operand = symbol_table[token.text]
                    elif token.type is TokenType.NUMBER:
                        operand = check_number(int(token.text), token.pos, line)
                    else:
                        raise AsmError(NUMBER_EXPECTED, token.pos, line)
                    if _pass == 2:
                        check_store(address, store, token.pos, line)
                        store[address] = operand
                    address += 1
                    token = next(iter)
                    if token.type not in END_OF_STATEMENT_TOKENS:
                        raise AsmError(EXTRA_GARBAGE, token.pos, line)
                elif token.type is TokenType.NAME:

                    mnemonic = token.text

                    # look up the opcode for this mnemonic
                    found = lookup_mnemonic(token.text)
                    if not found:
                        raise AsmError(BAD_MNEMONIC, token.pos, line)
                    opcode, instruction_type = found

                    token = next(iter)

                    if instruction_type in INSTRUCTION_ALIASES:
                        if token.type is not TokenType.REGISTER:
                            raise AsmError(BAD_REGISTER, token.pos, line)
                        mnemonic += f"_{token.text}"

                        token = next(iter)

                        if instruction_type is InstructionType.REGISTER_ALIAS_2:
                            # takes a second operand
                            if token.type != TokenType.COMMA:
                                raise AsmError(COMMA_EXPECTED, token.pos, line)
                            token = next(iter)

                        # look up the opcode for the modified mnemonic
                        found = lookup_mnemonic(mnemonic)
                        if not found:
                            raise AsmError(BAD_MNEMONIC, token.pos, line)
                        opcode, instruction_type = found

                    # add the opcode the to binary output
                    if _pass == 2:
                        check_store(address, store, token.pos, line)
                        store[address] = opcode
                    address += 1

                    if instruction_type in SINGLE_NIBBLE_INSTRUCTIONS:
                        # instructions without an operand
                        if token.type not in END_OF_STATEMENT_TOKENS:
                            raise AsmError(EXTRA_GARBAGE, token.pos, line)
                    else:
                        # instruction with an operand
                        operand = 0
                        if token.type is TokenType.NUMBER:
                            operand = int(token.text)
                        elif token.type is TokenType.NAME:
                            if _pass == 2:
                                if token.text not in symbol_table:
                                    raise AsmError(UNDEFINED_OPERAND, token.pos, line)
                                operand = symbol_table[token.text]
                        else:
                            raise AsmError(BAD_OPERAND, token.pos, line)
                        token = next(iter)
                        # check of offset
                        if token.type in (TokenType.PLUS, TokenType.MINUS):
                            operator_text = token.text
                            token = next(iter)
                            if token.type is not TokenType.NUMBER:
                                raise AsmError(NUMBER_EXPECTED, token.pos, line)
                            offset = check_number(int(token.text), token.pos, line)
                            if operator_text == "+":
                                operand += offset
                            else:
                                operand -= offset
                            operand &= 0xF
                            token = next(iter)
                        check_number(operand, token.pos, line)
                        if _pass == 2:
                            check_store(address, store, token.pos, line)
                            store[address] = operand
                        address += 1
                        if token.type not in END_OF_STATEMENT_TOKENS:
                            raise AsmError(EXTRA_GARBAGE, token.pos, line)
                else:
                    raise AsmError(SYNTAX_ERROR, token.pos, line)

    return store
