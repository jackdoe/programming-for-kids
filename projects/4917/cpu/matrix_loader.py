def load_matrix(file):
    state = []
    for line in file.readlines():
        if "#" in line:
            continue
        line = line.replace("│", " ")
        line = line.replace("_", " ")
        row = []
        for s in line.split():
            if s.isdigit():
                row.append(int(s))
        # remove first and last element in case its pasted from our output
        if len(row) == 6:
            row.pop(5)
            row.pop(0)
        if len(row) > 0:
            state += row
    file.close()
    return state
