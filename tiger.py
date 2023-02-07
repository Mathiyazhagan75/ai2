from heapq import heappush, heappop

def astar(start, goal, h):
    """A* search algorithm to solve the "Tiger, Farmer, Goat, Grass" problem.
    start: the starting state of the problem
    goal: the desired end state of the problem
    h: heuristic function to evaluate the distance between the current state and the goal state
    Returns: a list of actions to reach the goal state
    """
    heap = [(h(start, goal), 0, start, [])]
    visited = set()
    while heap:
        (f, g, state, path) = heappop(heap)
        if state in visited:
            continue
        visited.add(state)
        if state == goal:
            return path
        for next_state, action in successors(state):
            if next_state in visited:
                continue
            heappush(heap, (g + 1 + h(next_state, goal), g + 1, next_state, path + [action]))

def h(state, goal):
    """Heuristic function to evaluate the estimated distance between the current state and the goal state"""
    # count the number of mismatched elements in the two states
    return sum([s != g for s, g in zip(state, goal)])

def successors(state):
    """Generates all possible next states and the corresponding action that leads to that state"""
    # unpack the state elements into separate variables
    t, f, g, c = state
    # the farmer goes alone
    if f == "W":
        # farmer goes from west to east
        if t == "W":
            yield ("E", "E", g, "W"), "Farmer goes alone from West to East"
        # farmer goes from east to west
        else:
            yield ("W", "W", g, "E"), "Farmer goes alone from East to West"
    else:
        # farmer takes the tiger from west to east
        if t == "W":
            yield ("E", "E", g, c), "Farmer takes the Tiger from West to East"
        # farmer takes the tiger from east to west
        else:
            yield ("W", "W", g, c), "Farmer takes the Tiger from East to West"
        # farmer takes the goat from west to east
        if g == "W":
            yield (t, "E", "E", c), "Farmer takes the Goat from West to East"
        # farmer takes the goat from east to west
        else:
            yield (t, "W", "W", c), "Farmer takes the Goat from East to West"
        # farmer takes the grass from west to east
        if c == "W":
            yield (t, "E", g, "E"), "Farmer takes the Grass from West to East"
        # farmer takes the grass from east to west
        else:
            yield (t, "W", g, "W"), "Farmer takes the Grass from East to West"

# Example usage:
start = ("W", "W", "W", "W")
goal = ("E", "E", "E", "E")
path