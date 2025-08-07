from algorithms.sorting import quicksort
from problems.maze_solver import solve_maze

if __name__ == "__main__":
    print("1. Sort List")
    print("2. Solve Maze")
    choice = input("Enter choice: ")

    if choice == "1":
        lst = list(map(int, input("Enter numbers: ").split()))
        print("Sorted:", quicksort(lst))
    
    elif choice == "2":
        maze = [
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 1, 0, 0],
            [1, 0, 0, 0]
        ]
        print("Path exists?" , solve_maze(maze, (0,0), (3,3)))
