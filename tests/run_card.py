import os
import re
import sys
from io import StringIO

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
