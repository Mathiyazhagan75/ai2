n = 3

class Puzzle:
    def __init__(self, puzzle, level, fVal, goal):
        self.puzzle = puzzle
        self.level = level
        self.fVal = fVal
        self.goal = goal
        self.n = n
        
    def findF(self):
        return self.findH()+self.level

    def findH(self):
        cou = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if self.puzzle[i][j] != self.goal[i][j] and self.puzzle[i][j] != 0:
                    cou += 1
        return cou
    
    def find(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.puzzle[i][j] == 0:
                    return [i, j]
                
    def swap(self, x1, y1, x2, y2):
        if not (x2 >= 0 and x2 < self.n and y2 >= 0 and y2 < self.n):
            return None
        
        child = []
        
        for i in range(self.n):
            c = []
            for j in range(self.n):
                c.append(self.puzzle[i][j])
            child.append(c)
        
        child[x1][y1], child[x2][y2] = child[x2][y2], child[x1][y1]
        
        return child
            
        
    
    def generate(self):
        x, y = self.find()
        options = [[x, y-1], [x, y+1], [x-1, y], [x+1, y]]
        expanded = []
        
        for i in options:
            child = self.swap(x, y, i[0], i[1])
            
            if child != None:
                expanded.append(Puzzle(child, self.level+1, 0, self.goal))
        
        return expanded
            
    
    def display(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.puzzle[i][j], end=" ")
            print("")
        print("\n\n")
    

expanded = []

initial = [[1, 2, 3],
           [0, 4, 6],
           [7, 5, 8]]

final = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]]

start = Puzzle(initial, 0, 0, final)
start.fVal = start.findF()

expanded.append(start)

while True:
    cur = expanded[0]
    
    cur.display()
    
    if cur.findH() == 0:
        break
    
    for i in cur.generate():
        i.fVal = i.findF()
        expanded.append(i)
        
    del expanded[0]
    
    expanded.sort(key = lambda x:x.fVal)
    

    
    