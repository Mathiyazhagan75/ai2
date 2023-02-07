from heapq import heappush, heappop

def astar(start, goal, h):
    """A* search algorithm to solve the water jug problem.
    start: tuple representing the starting state of the jugs
    goal: tuple representing the desired end state of the jugs
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
    return sum(abs(state[i] - goal[i]) for i in range(len(state)))

def successors(state):
    """Generates all possible next states and the corresponding action that leads to that state"""
    x, y = state
    # fill jug x
    yield (CAPACITY_X, y), "Fill jug X"
    # fill jug y
    yield (x, CAPACITY_Y), "Fill jug Y"
    # empty jug x
    yield (0, y), "Empty jug X"
    # empty jug y
    yield (x, 0), "Empty jug Y"
    # pour water from x to y
    amount = min(x, CAPACITY_Y - y)
    yield (x - amount, y + amount), f"Pour {amount} units from X to Y"
    # pour water from y to x
    amount = min(y, CAPACITY_X - x)
    yield (x + amount, y - amount), f"Pour {amount} units from Y to X"

# Example usage:
CAPACITY_X = 4
CAPACITY_Y = 3
start = (0, 0)
goal = (2, 0)
path = astar(start, goal, h)
print(path)
