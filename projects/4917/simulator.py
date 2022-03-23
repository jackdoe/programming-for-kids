import sys
import argparse

from cpu.assembler import assemble, AsmError
from cpu.disassembler import disassemble
from cpu.cpu import cpu
from cpu.matrix_loader import load_matrix
from cpu.ascii_visualizer import ascii


def main():
    parser = argparse.ArgumentParser(description="4917 CPU Simulator")
    parser.add_argument("filename", type=str, help="Program file (.prg or .asm)")
    parser.add_argument(
        "-v",
        "--visualize",
        help="Visualizer to use",
        choices=["asm", "matrix"],
        default=None,
    )
    parser.add_argument(
        "-d",
        "--debug",
        help="Turn debugger on/off",
        choices=["on", "off"],
        default="on",
    )

    args = parser.parse_args()
    filename = args.filename
    visualize = args.visualize

    if not args.filename:
        print("No filename specified.")
        exit(1)

    if filename.endswith(".prg"):
        if not visualize:
            visualize = "matrix"
    elif filename.endswith(".asm"):
        if not visualize:
            visualize = "asm"
    else:
        print("Unsupported file type.")

    visualizer = disassemble if visualize == "asm" else ascii
    debug = args.debug == "on"

    filename = args.filename

    # for debugging purposes:
    # filename = r".\projects\4917\deck\02.prg"
    # visualizer = disassemble
    # debug = True

    try:
        with open(filename) as file:
            if filename.endswith(".prg"):
                IP, IS, RO, R1, *memory = load_matrix(file)
            else:
                memory = assemble(file)
            cpu(visualizer, memory, debug=debug)
    except AsmError as exc:
        print(exc.message)
    except Exception as exc:
        print(exc)


if __name__ == "__main__":
    main()
