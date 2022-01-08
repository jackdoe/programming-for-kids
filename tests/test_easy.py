"""Test suite for easy deck"""
import os
import sys
from io import StringIO

PLACE_HOLDER = "⚂"


def run_card(file_name, values=range(1, 21)):
    """Returns a list of printed lines"""
    file_path = os.path.normpath(
        os.path.join(
            sys.path[0], "../projects/programming-time/decks/easy", file_name + ".py"
        )
    )
    prog_text = open(file_path, "r", encoding="utf-8").read()

    value_index = 0
    while prog_text.find(PLACE_HOLDER) != -1:
        prog_text = prog_text.replace(PLACE_HOLDER, str(values[value_index]), 1)
        value_index += 1

    old_stdout = sys.stdout
    sys.stdout = my_stdout = StringIO()

    exec(prog_text)

    sys.stdout = old_stdout
    return my_stdout.getvalue().strip().split("\n")


def test_01():
    """gcd"""
    output = run_card("01", [12, 16])
    assert output[-1] == "4"


def test_02():
    """Diffie–Hellman Key Exchange"""
    output = run_card("02", [15, 7])
    assert output[-1] == "Shared Secret: 15 15"
