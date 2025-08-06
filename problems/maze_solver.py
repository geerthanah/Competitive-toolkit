from collections import deque

def solve_maze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set([start])
    directions = [(0,1),(1,0),(-1,0),(0,-1)]

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return False
