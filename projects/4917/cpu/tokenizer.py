import re
from dataclasses import dataclass
from enum import Enum, auto


class TokenType(Enum):
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
    OTHER = auto()


@dataclass
class Token:
    type: TokenType
    text: str
    pos: int


token_patterns = [
    (TokenType.DIRECTIVE, re.compile(r"\.([A-Z]+)", re.IGNORECASE)),
    (TokenType.LABEL, re.compile(r"([A-Z]\w*):", re.IGNORECASE)),
    (TokenType.REGISTER, re.compile(r"(R[01])", re.IGNORECASE)),
    (TokenType.NAME, re.compile(r"([A-Z]\w*)", re.IGNORECASE)),
    (TokenType.LOCATION, re.compile(r"(\d+):")),
    (TokenType.NUMBER, re.compile(r"(\d+)")),
    (TokenType.COMMA, re.compile(r"(,)")),
    (TokenType.PLUS, re.compile(r"(\+)")),
    (TokenType.MINUS, re.compile(r"(-)")),
    (TokenType.COMMENT, re.compile(r"(\s*;)")),
    (TokenType.WHITESPACE, re.compile(r"(\s+)")),
    (TokenType.OTHER, re.compile(r"(.)")),
]


def tokenizer(line):
    start = 0
    stop = len(line)
    while start < stop:
        for type, pattern in token_patterns:
            match = pattern.match(line, start)
            if match:
                if type is not TokenType.WHITESPACE:
                    text = match.group(1).upper()
                    yield Token(type, text, start)
                start = match.end()
                break
        else:
            raise Exception("Logic error in tokenizer")
    yield Token(TokenType.EOL, "", 0)
