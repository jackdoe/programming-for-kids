def ascii(state, highlight):
    IP, IS, R0, R1, memory = state

    center = []
    for (i, s) in enumerate((IP, IS, R0, R1, *memory)):
        if i - 4 in highlight:
            s = "_" + str(s) + "_"
        center.append(str(s).center(4))

    print(
        """
    ┌────────┐ ┌────────┐
    │IP: {0}│ │IS: {1}│
    └────────┘ └────────┘
    ┌────────┐ ┌────────┐
    │R0: {2}│ │R1: {3}│
    └────────┘ └────────┘

    ┌────┬────┬────┬────┐
  0 │{4}│{5}│{6}│{7}│ 3
    ├────┼────┼────┼────┤
  4 │{8}│{9}│{10}│{11}│ 7
    ├────┼────┼────┼────┤
  8 │{12}│{13}│{14}│{15}│ 11
    ├────┼────┼────┼────┤
 12 │{16}│{17}│{18}│{19}│ 15
    └────┴────┴────┴────┘  

""".format(
            *center
        )
    )

    input("hit enter to continue> ")
