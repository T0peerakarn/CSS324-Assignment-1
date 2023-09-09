def initial_state():
    return (8, 0, 0)


def is_goal(s):
    return s == (4, 4, 0)


def successors(s):

    capacity = (8, 5, 3)

    for i in range(3):
        for j in range(3):

            if i == j: continue

            t = min(s[i], capacity[j] - s[j])
            if t == 0: continue

            d = [0, 0, 0]
            d[i], d[j] = -t, t

            yield (tuple([s[k] + d[k] for k in range(3)]), t)
