"""
Test suite for easy deck

If needed, install pytest: pip install pytest

Then run the command: pytest
"""
import datetime
import math
import re

import pytest

from run_card import run_card


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


def test_12():
    """bloom filters"""
    output = run_card("12", [10, 11, 12, 13])
    result = output[-1]
    assert result == "we might have seen it"

    output = run_card("12", [1, 2, 4, 5])
    result = output[-1]
    assert result == "we have never seen it"


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


def test_26():
    output = run_card("26", [10,11,12])
    assert output[0] == "0 0"
    assert output[1] == "4 1"
    assert output[2] == "5 1"
    assert output[3] == "3 1"
    assert output[4] == "2 0"

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


def test_36():
    """list concatenation"""
    output = run_card("36", [1, 2, 3, 4])
    result = int(output[-1])
    assert result == 5


def test_37():
    """homebrew integer division"""
    output = run_card("37", [13, 6])
    remainder = int(output[-1])
    assert remainder == 1


def test_38():
    """off-origin cartesian quadrants"""
    output = run_card("38", [1, 1])
    assert output[-1] == "A"

    output = run_card("38", [1, 20])
    assert output[-1] == "B"

    output = run_card("38", [20, 1])
    assert output[-1] == "D"

    output = run_card("38", [20, 20])
    assert output[-1] == "C"

    output = run_card("38", [5, 4])
    assert output[-1] == "P"

    output = run_card("38", [5, 1])
    assert output[-1] == "on a line"


def test_39():
    """split string on separator"""
    output = run_card("39", [ord("a") - 96])
    splitted = output[-1]
    assert splitted == "hellothisispython"

    output = run_card("39", [ord("l") - 96])
    splitted = output[-1]
    assert splitted == "he"

    output = run_card("39", [ord("i") - 96])
    splitted = output[-1]
    assert splitted == "helloth"


def test_40():
    """primitive value representations"""
    output = run_card("40", [20, 20])
    assert output[-1] == "True"

    output = run_card("40", [1, 20])
    assert output[-1] == "False"


def test_41():
    """approximate e and pi"""
    output = run_card("41", [3, 3])
    values = output[-1].split(" ")
    e = float(values[0])
    pi = float(values[1])
    print(e, pi)
    assert e == pytest.approx(math.e, abs=0.1)
    assert pi == pytest.approx(math.pi, abs=0.1)


def test_42():
    """tic-tac-toe"""
    output = run_card("42", [1])
    assert output[-1] == "-"

    output = run_card("42", [2])
    assert output[-1] == "x"


def test_43():
    """client/server"""
    output = run_card("43", [12])
    sent = int(output[-2].split(":")[1])
    recv = int(output[-1].split(":")[1])
    assert sent == 12
    assert recv == 24


def test_44():
    """object references"""
    output = run_card("44", [11])
    b_0 = int(output[-1])
    assert b_0 == 11


def test_45():
    """observer pattern"""
    output = run_card("45", [1])
    assert output[-1] == "down"

    output = run_card("45", [11])
    assert output[-1] == "up"


def test_46():
    """list reversal"""
    output = run_card("46", [1, 2, 3])
    b = eval(output[-2])
    c = eval(output[-1])
    assert b == [3, 2, 1]
    assert c == [3, 2, 1]


def test_47():
    """slicing"""
    output = run_card("47", [5])
    l = int(output[-1])
    assert l == 5


def test_48():
    """homebrew Range interable"""
    output = run_card("48", [1])
    assert int(output[0]) == 0
    assert int(output[-1]) == 24

    output = run_card("48", [7])
    assert int(output[0]) == 0
    assert int(output[-1]) == 21


def test_49():
    """run length encoding"""
    output = run_card("49", [1])
    compressed = eval(output[-1])
    assert compressed == [1, 10, 2, 1, 3, 2]

    output = run_card("49", [2])
    compressed = eval(output[-1])
    assert compressed == [1, 11, 3, 2]


def test_50():
    """hash table"""
    output = run_card("50", [1, 2, 3])
    assert int(output[-1]) == 2

    output = run_card("50", [1, 2, 7])
    assert int(output[-1]) == 1


def test_51():
    """linked list"""
    output = run_card("51", [1, 2, 3])
    assert int(output[-3]) == 3
    assert int(output[-2]) == 2
    assert int(output[-1]) == 1


def test_52():
    """binary search"""
    output = run_card("52", [9])
    assert "4" in output[-1]

    output = run_card("52", [10])
    assert output[-1] == "not found"


def test_53():
    """classes"""
    output = run_card("53", [3, 7])
    assert "max" in output[-1]
    assert output[-2] == "Max Woof!"
    assert output[-3] == "Ruffles oof!"


def test_54():
    """class Rect, hit testing"""
    output = run_card("54", [11, 11])
    assert output[-1] == "outside"

    output = run_card("54", [11, 9])
    assert output[-1] == "inside"

    output = run_card("54", [11, 3])
    assert output[-1] == "inside"

    output = run_card("54", [11, 2])
    assert output[-1] == "outside"

    output = run_card("54", [9, 9])
    assert output[-1] == "outside"

    output = run_card("54", [14, 9])
    assert output[-1] == "inside"

    output = run_card("54", [15, 9])
    assert output[-1] == "outside"
