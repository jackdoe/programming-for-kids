#    0 halt
#    1 add R0 = R0 + R1, 2 subtract R0 = R0 - R1
#    3 inc R0, 4 inc R1
#    5 dec R0, 6 dec R1
#    7 ring bell
#  8 X print X
#  9 X R0 = mem[X]
# 10 X R1 = mem[X]
# 11 X mem[X] = R0
# 12 X mem[X] = R1
# 13 X jump to address X
# 14 X jump to address X if R0 == 0
# 15 X jump to address X if R0 != 0
#
# jumpy

┌────────┐ ┌────────┐
│ IP:  0 │ │ IS:  0 │
└────────┘ └────────┘
┌────────┐ ┌────────┐
│ R0:  0 │ │ R1:  0 │
└────────┘ └────────┘

┌────┬────┬────┬────┐
│ 13 │  2 │ 13 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  0 │
├────┼────┼────┼────┤
│  0 │  0 │  0 │  0 │
└────┴────┴────┴────┘
