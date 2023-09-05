def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4


def successors(s):
    x, y, z = s

    # x -> y
    t = min(5-y, x)
    if t != 0: yield ((x-t, y+t, z), t)

    # x -> z
    t = min(3-z, x)
    if t != 0: yield ((x-t, y, z+t), t)

    # y -> x
    t = min(8-x, y)
    if t != 0: yield ((x+t, y-t, z), t)

    # y -> z
    t = min(3-z, y)
    if t != 0: yield ((x, y-t, z+t), t)

    # z -> x
    t = min(8-x, z)
    if t != 0: yield ((x+t, y, z-t), t)

    # z -> y
    t = min(5-y, z)
    if t != 0: yield ((x, y+t, z-t), t)
