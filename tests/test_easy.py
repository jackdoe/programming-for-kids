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
    output = run_card("01", [12, 16])
    result = int(output[-1])
    assert result == 4


def test_02():
    """Diffie-Hellman Key Exchange"""
    output = run_card("02", [15, 7])

    # Example output: Shared Secret: 15 15
    match = re.search(r"(\d+).+?(\d+)", output[-1])
    assert match is not None
    secret_ab = match.group(1)
    secret_ba = match.group(2)

    # shared secrets from both parties must match
    assert secret_ab == secret_ba


def test_03():
    """is_prime"""
    output = run_card("03", [1])
    assert output[-1] == "not a prime"

    output = run_card("03", [2])
    assert output[-1] == "prime"

    output = run_card("03", [4])
    assert output[-1] == "not a prime"

    output = run_card("03", [13])
    assert output[-1] == "prime"


def test_04():
    """RSA algorithm"""
    output = run_card("04", [17])

    # recreate message as done in card
    message = 50 + 17
    decrypted = int(output[-1])
    assert decrypted == message


def test_05():
    """sum & average"""
    output = run_card("05", [10, 11, 12])
    average = float(output[-1])
    assert average == 11


def test_06():
    """square root"""
    output = run_card("06", [1])
    area = float(output[-1])
    assert area == 32


def test_07():
    """remove() element from list"""
    output = run_card("07", [1, 2])
    winner = output[-1]
    assert winner == "penny"


def test_08():
    """quadrant"""
    output = run_card("08", [11, 11])
    assert int(output[-1]) == 1

    output = run_card("08", [11, 9])
    assert int(output[-1]) == 4

    output = run_card("08", [9, 9])
    assert int(output[-1]) == 3

    output = run_card("08", [9, 11])
    assert int(output[-1]) == 2

    output = run_card("08", [10, 10])
    assert int(output[-1]) == 0


def test_09():
    """import"""
    now = datetime.datetime.now()
    meeting_time = 10
    output = run_card("09", [meeting_time])

    expected = "on time" if now.minute < meeting_time else "you are late"
    assert output[-1] == expected


def test_10():
    """Reverse Polish Notation"""
    output = run_card("10", [10, 11, 12])
    result = float(output[-1])
    expected = (10 + 11) * 12
    assert result == pytest.approx(expected)


def test_11():
    """encryption by transposition"""
    message = [1, 2, 3]
    output = run_card("11", message)
    assert output[-1] == "nop"


# test_12(): not implemented due to package requirement


def test_13():
    """Haunted house"""
    output = run_card("13", [3, 6, 1, 3])
    assert output[-2] == "RUUUNNN!!"
    assert output[-1] == "phew! no ghost!"


def test_14():
    """sort / reverse"""
    output = run_card("14", [3, 5, 2])
    a_0 = int(output[-1])
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
    output = run_card("16", [1])
    assert "Magenta pink" in output[-1]


def test_17():
    """lambda functions"""
    output = run_card("17", [13, 5])
    result = int(output[-1])
    assert result == 13


def test_18():
    """mixed scope"""
    output = run_card("18", [11])
    x = int(output[-1])
    assert x == 11


def test_19():
    """global scope"""
    output = run_card("19", [11])
    x = int(output[-1])
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
    output = run_card("22", [11])
    result = int(output[-1])
    assert result == 121


def test_23():
    """howebrew arithmetic primitives"""
    output = run_card("23", [9, 8])
    result = int(output[-1])
    assert result == 1000


def test_24():
    """dict lookup"""
    output = run_card("24", [2])
    assert output[-1] == "b"


def test_25():
    """fizbuzz"""
    output = run_card("25", [1])
    assert output[-1] == "1"

    output = run_card("25", [3])
    assert output[-1] == "fizz"

    output = run_card("25", [5])
    assert output[-1] == "buzz"

    output = run_card("25", [15])
    assert output[-1] == "fizzbuzz"

    output = run_card("25", [19])
    assert output[-1] == "19"


# test_25(): not implemented due to package requirement


def test_27():
    """morse code"""
    output = run_card("27", [4])
    assert output[-1] == ".-.."  # letter l


def test_28():
    """break"""
    output = run_card("28", [11, 7])
    result = int(output[-1])
    assert result == 25  # 12 + 13


def test_29():
    """reduce"""
    output = run_card("29", [13])
    result = float(output[-1])
    assert result == pytest.approx(7.5)


def test_30():
    """Rock, Paper, Scissors"""
    output = run_card("30", [3, 1, 3, 2, 3, 3, 4, 1, 4, 2, 4, 3, 5, 1])
    wins_a = int(output[-2])
    wins_b = int(output[-1])
    assert wins_a == 3
    assert wins_b == 2


def test_31():
    """strings in memory"""
    output = run_card("31", [1])
    assert output[-1] == "aoi"


def test_32():
    """find element in collection"""
    output = run_card("32", [1])
    assert output[-1] == "work work"

    output = run_card("32", [5])
    assert output[-1] == "yey, weekend"

    output = run_card("32", [19])
    assert output[-1] == "oops, expected 0 to 6"


def test_33():
    """pop element from list"""
    output = run_card("33", [1, 2, 3])
    result = int(output[-1])
    assert result == 2


def test_34():
    """Bayes' Theorem"""
    output = run_card("34", [10])
    P_computed = float(output[-1])
    P_expected = 100 * (0.1 * 0.6) / (0.5 + 10 / 100)
    assert P_computed == pytest.approx(P_expected)


def test_35():
    """homebrew log"""
    output = run_card("35", [3])
    result = int(output[0])
    assert result == 10


if __name__ == "__main__":
    test_21()
