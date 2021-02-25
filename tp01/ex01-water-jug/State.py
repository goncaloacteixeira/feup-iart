class State:
    def __init__(self, initial, final, info, cost=1):
        self.initial = initial
        self.final = final
        self.info = info
        self.cost = cost

    def __str__(self):
        return str(self.initial) + " - " + self.info + " - " + str(self.final) + " :: Cost - " + str(self.cost)


def expand(operation: State):
    (x, y) = operation.final

    expanded = []

    if x + y >= 4 and y > 0:
        if x != 4 or y != y - (4 - x):
            expanded.append(State(operation.final, (4, y - (4 - x)),
                                  "Pour water from the 3L bucket to completely fill the 4L bucket"))
    if x + y >= 3 and x > 0:
        if x != x - (3 - y) or y != 3:
            expanded.append(State(operation.final, (x - (3 - y), 3),
                                  "Pour water from the 4L bucket to completely fill the 3L bucket"))
    if x + y <= 4 and y > 0:
        if x != x + y or y != 0:
            expanded.append(
                State(operation.final, (x + y, 0), "Pour all the water from the 3L bucket to the 4L bucket"))
    if x + y <= 3 and x > 0:
        if x != 0 or y != x + y:
            expanded.append(
                State(operation.final, (0, x + y), "Pour all the water from the 4L bucket to the 3L bucket"))
    if x < 4:
        expanded.append(State(operation.final, (4, y), "Fill the 4L bucket"))
    if y < 3:
        expanded.append(State(operation.final, (x, 3), "Fill the 3L bucket"))
    if x > 0:
        expanded.append(State(operation.final, (0, y), "Empty the 4L bucket"))
    if y > 0:
        expanded.append(State(operation.final, (x, 0), "Empty the 3L bucket"))

    for state in expanded:
        state.parent = operation

    return expanded
