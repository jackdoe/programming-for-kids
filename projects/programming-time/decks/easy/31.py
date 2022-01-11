# ┌──────────────────────┐
# │ computer memory      │
# │...2 1 ?..............│ 0  - 21
# │...▲..................│ 22 - 43
# └───┼──────────────────┘
#     │ addr: 3, ? is 96 + ⚂
# x ──┘
#
# Strings are immutable in python,
# which means they can't be changed.
# ┌──────────────────────┐
# │...2 1 ?..............│ 0  - 21
# │...........2 2 ? 111..│ 22 - 43
# │....2 3 ? 111 105.....│ 44 - 65
# └────┼─────────────────┘
#      │ addr: 49
# x ───┘
#
# Three strings will be created one
# for '?', '?o' and '?oi', in the
# end the variable x will point to
# the last one. The unused strings
# will have nothing pointing to
# them, and the garbage collector
# will reclaim the memory, so it can
# be used again by your program.

x = chr(96 + ⚂)
x = x + 'o'
x = x + 'i'
print(x)
