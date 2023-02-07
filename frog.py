from heapq import heappush, heappop

def astar(start, goal, h):
    """A* search algorithm to solve the frog jump problem.
    start: the starting position of the frog
    goal: the desired end position of the frog
    h: heuristic function to evaluate the distance between the current position and the goal position
    Returns: a list of actions to reach the goal position
    """
    heap = [(h(start, goal), 0, start, [])]
    visited = set()
    while heap:
        (f, g, position, path) = heappop(heap)
        if position in visited:
            continue
        visited.add(position)
        if position == goal:
            return path
        for next_position, action in successors(position):
            if next_position in visited:
                continue
            heappush(heap, (g + 1 + h(next_position, goal), g + 1, next_position, path + [action]))

def h(position, goal):
    """Heuristic function to evaluate the estimated distance between the current position and the goal position"""
    return abs(position - goal)

def successors(position):
    """Generates all possible next positions and the corresponding action that leads to that position"""
    # jump one step to the right
    yield position + 1, "Jump right by 1 step"
    # jump two steps to the right
    yield position + 2, "Jump right by 2 steps"
    # jump one step to the left
    if position - 1 >= 0:
        yield position - 1, "Jump left by 1 step"
    # jump two steps to the left
    if position - 2 >= 0:
        yield position - 2, "Jump left by 2 steps"

# Example usage:
start = 0
goal = 10
path = astar(start, goal, h)
print(path)