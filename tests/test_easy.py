"""
Test suite for easy deck

If needed, install pytest: pip install pytest

Then run the command: pytest
"""
import datetime
import os
import re
import sys
from io import StringIO

import pytest

PLACE_HOLDER = "⚂"

GET_VALUE_CODE_SNIPPET = """
index = 0
def get_value():
    global index
    global values
    value = values[index % len(values)]
    index += 1
    return value

"""


def run_card(file_name, values=range(1, 21)):
    """Returns a list of printed lines"""
    file_path = os.path.normpath(
        os.path.join(
            sys.path[0], "../projects/programming-time/decks/easy", file_name + ".py"
        )
    )

    with open(file_path, "r", encoding="utf-8") as file:
        lines = []
        for line in file:
            line = line.rstrip()
            # remove blank and comment lines
            if line != "" and not re.match(r"^\s*#", line):
                lines.append(line)
        prog_text = "\n".join(lines)

    # replace PLACE_HOLDER symbols with a call to get_value()
    prog_text = prog_text.replace(PLACE_HOLDER, "get_value()")

    # add code snippets for values list and get_value function
    prog_text = f"\nvalues = {list(values)}\n" + GET_VALUE_CODE_SNIPPET + prog_text

    # capture stdout output
    old_stdout = sys.stdout
    sys.stdout = my_stdout = StringIO()

    # pylint: disable = exec-used
    exec(prog_text, dict())

    sys.stdout = old_stdout
    return my_stdout.getvalue().strip().split("\n")


def test_01():
    """gcd"""
    *_, output = run_card("01", [12, 16])
    assert int(output) == 4


def test_02():
    """Diffie-Hellman Key Exchange"""
    *_, output = run_card("02", [15, 7])

    # Example output: Shared Secret: 15 15
    match = re.search(r"(\d+).+?(\d+)", output)
    assert match is not None
    secret_ab = match.group(1)
    secret_ba = match.group(2)

    # shared secrets from both parties must match
    assert secret_ab == secret_ba


def test_03():
    """is_prime"""
    *_, output = run_card("03", [1])
    assert output == "not a prime"

    *_, output = run_card("03", [2])
    assert output == "prime"

    *_, output = run_card("03", [4])
    assert output == "not a prime"

    *_, output = run_card("03", [13])
    assert output == "prime"


def test_04():
    """RSA algorithm"""
    die = 17
    *_, output = run_card("04", [die])

    # recreate message as done in card
    message = 50 + 17
    decrypted = int(output)
    assert decrypted == message


def test_05():
    """sum & average"""
    *_, output = run_card("05", [10, 11, 12])
    average = float(output)
    assert average == 11


def test_06():
    """square root"""
    *_, output = run_card("06", [1])
    area = float(output)
    assert area == 32


def test_07():
    """remove() element from list"""
    *_, winner = run_card("07", [1, 2])
    assert winner == "penny"


def test_08():
    """quadrant"""
    *_, output = run_card("08", [11, 11])
    assert int(output) == 1

    *_, output = run_card("08", [11, 9])
    assert int(output) == 4

    *_, output = run_card("08", [9, 9])
    assert int(output) == 3

    *_, output = run_card("08", [9, 11])
    assert int(output) == 2

    *_, output = run_card("08", [10, 10])
    assert int(output) == 0


def test_09():
    """import"""
    now = datetime.datetime.now()
    meeting_time = 10
    *_, output = run_card("09", [meeting_time])

    expected = "on time" if now.minute < meeting_time else "you are late"
    assert output == expected


def test_10():
    """Reverse Polish Notation"""
    *_, output = run_card("10", [10, 11, 12])
    expected = (10 + 11) * 12
    assert float(output) == expected


def test_11():
    """encryption by transposition"""
    message = [1, 2, 3]
    *_, output = run_card("11", message)
    assert output == "nop"


# test_12(): not implemented due to package requirement


def test_13():
    """Haunted house"""
    output = run_card("13", [3, 6, 1, 3])
    assert output[-2] == "RUUUNNN!!"
    assert output[-1] == "phew! no ghost!"


def test_14():
    """sort / reverse"""
    *_, output = run_card("14", [3, 5, 2])
    a_0 = int(output)
    assert a_0 == 5


def test_15():
    """recursion"""
    output = run_card("15", [1, 3, 4, 3, 8])
    enemy_hp = int(output[-2])
    my_hp = int(output[-1])
    assert enemy_hp == -4
    assert my_hp == 16


def test_16():
    """dictionary lookup"""
    *_, output = run_card("16", [1])
    assert "Magenta pink" in output


def test_17():
    """lambda functions"""
    *_, output = run_card("17", [13, 5])
    result = int(output)
    assert result == 13


def test_18():
    """mixed scope"""
    *_, output = run_card("18", [11])
    x = int(output)
    assert x == 11


def test_19():
    """global scope"""
    *_, output = run_card("19", [11])
    x = int(output)
    assert x == 3


def test_20():
    """compare strings"""
    output = run_card("20", [1])
    # strings are equal => two lines should be printed
    assert len(output) == 2

    output = run_card("20", [1, 2, 3, 4])
    # strings are not equal => only one lines should be printed
    assert len(output) == 1


def test_21():
    """delta encoding"""
    output = run_card("21", [13])

    numbers = [int(x) for x in output[-2][1 : len(output[-2]) - 1].split(", ")]
    assert numbers == [1, 1, 1, 1, 1, 1, -3]


def test_22():
    """string to int"""
    *_, output = run_card("22", [11])
    result = int(output)
    assert result == 121


def test_23():
    """arithmetic primitives"""
    *_, output = run_card("23", [9, 8])
    result = int(output)
    assert result == 1000


def test_24():
    """dict lookup"""
    *_, output = run_card("24", [2])
    assert output == "b"


def test_25():
    """fizbuzz"""
    *_, output = run_card("25", [1])
    assert output == "1"

    *_, output = run_card("25", [3])
    assert output == "fizz"

    *_, output = run_card("25", [5])
    assert output == "buzz"

    *_, output = run_card("25", [15])
    assert output == "fizzbuzz"

    *_, output = run_card("25", [19])
    assert output == "19"


# test_25(): not implemented due to package requirement


def test_27():
    """morse code"""
    *_, output = run_card("27", [4])
    assert output == ".-.."  # letter l


def test_28():
    """break"""
    *_, output = run_card("28", [11, 7])
    result = int(output)
    assert result == 25  # 12 + 13


def test_29():
    """reduce"""
    *_, output = run_card("29", [13])
    result = float(output)
    assert result == pytest.approx(7.5)


if __name__ == "__main__":
    test_21()
