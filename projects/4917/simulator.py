import sys
import argparse

from cpu.assembler import assemble
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
        default="asm",
    )

    args = parser.parse_args()

    if not args.filename:
        print("No filename specified.")
        exit(1)

    if not (args.filename.endswith(".prg") or args.filename.endswith(".asm")):
        print("Unsupported file type")

    print(args)

    visualizer = disassemble if args.visualize == "asm" else ascii

    file = open(args.filename)
    if args.filename.endswith(".prg"):
        IP, IS, RO, R1, *memory = load_matrix(file)
        cpu(visualizer, memory, IP, RO, R1)
    else:
        memory = assemble(file)
        cpu(visualizer, memory)


if __name__ == "__main__":
    main()
