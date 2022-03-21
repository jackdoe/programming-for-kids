from cpu.instruction_set import instruction_set, InstructionType


def exec_instruction(state, instruction):
    IP, R0, R1, memory = state
    microcode, type = instruction

    if type == InstructionType.REGISTER:
        # register instruction
        R0, R1 = microcode(R0, R1)
    elif type == InstructionType.MEMORY:
        # memory instruction
        R0, R1, memory = microcode(R0, R1, IP, memory)
        IP += 1
    elif type == InstructionType.BRANCH:
        # branch instruction
        IP = microcode(IP, R0, memory)
    elif type == InstructionType.STATELESS:
        # stateless instruction
        microcode()
    else:
        raise Exception(f"Invalid instruction type: {type}")

    # truncate registers to 4 bits (all are unsigned nibbles)
    IP, R0, R1 = (register & 0xF for register in (IP, R0, R1))

    return IP, R0, R1, memory


def cpu(
    visualizer,
    memory,
    IP=0,
    R0=0,
    R1=0,
    debug=True,
):
    IS = 0

    while True:

        # Fetch the next instruction
        IS = memory[IP]

        highlight = [IP]
        if IS >= 8:
            highlight = [IP, (IP + 1) & 0xF]

        if debug:
            visualizer((IP, IS, R0, R1, memory), highlight)

        # Increment the instruction pointer
        IP = (IP + 1) & 0xF

        # Lookup the function to execute and the width of the instruction
        instruction = instruction_set[IS]

        state = IP, R0, R1, memory
        state = exec_instruction(state, instruction)
        IP, R0, R1, memory = state

        # Exit the for the HLT instruction
        if IS == 0:
            break

    if debug:
        visualizer((IP, IS, R0, R1, memory), highlight)
