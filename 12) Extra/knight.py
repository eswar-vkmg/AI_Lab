from collections import deque

def isSafe(x, y):
    global visited
    if((x, y) in visited or x<0 or y<0 or x>7 or y>7):
        return False
    return True

def knight(src, dest):
    q = deque([(src, 0)])
    possiblities = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    
    while(q):
        curr = q.popleft()
        curr_pos, curr_lvl = curr[0], curr[1]        
        x, y = curr_pos
        
        for dx, dy in possiblities:
            x_new, y_new = x + dx, y + dy
            if(isSafe(x_new, y_new)):
                parent[(x_new, y_new)] = (x, y)
                if((x_new, y_new) == dest):
                    return curr_lvl + 1
                else:
                    q.append(((x_new, y_new), curr_lvl + 1))
                       
def printPath(parent, curr):
    if(curr == (-1, -1)):
        return
    printPath(parent, parent[curr])
    print(curr, end = " ")
        

if __name__ == "__main__":
    src, dest = (3, 4), (6, 3)
    visited, parent = set(), dict()
    print("\nNumber of steps needed = ", knight(src, dest))
    parent[src] = (-1, -1)
    curr = list(parent.keys())[-1]
    print("\nPath followed = ", end = " ")
    printPath(parent, curr)
