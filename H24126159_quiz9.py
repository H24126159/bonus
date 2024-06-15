import random

def parse_maze_file(filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            
            # Calculate the number of rows and columns
            N = int((len(lines) - 1) / 2)
            M = int((len(lines[0]) - 1) / 4)
            
            # Initialize maze
            maze = {}
            for i in range(N):
                for j in range(M):
                    if lines[2*i + 1][4*j + 2] == 'X': # 如果原始檔案裡面有"X"要保留為障礙
                        maze[(i, j)] = 1 # 1是障礙
                    else:
                        maze[(i, j)] = 0 # 設定為空白
            return maze, N, M
    except IOError:
        raise
    except Exception as e:
        print(f"Error: {e}")
        raise

def generate_path(maze, N, M):
    path = [(0, 0)]
    i, j = 0, 0
    maze[(0, 0)] = 2

    while (i, j) != (N-1, M-1):
        if i == N-1:
            j += 1
        elif j == M-1:
            i += 1
        else:
            if random.choice([True, False]): # 隨機選擇path
                if j + 1 < M and maze[(i, j + 1)] == 0:
                    j += 1
                elif i + 1 < N and maze[(i + 1, j)] == 0:
                    i += 1
                else:
                    break
            else:
                if i + 1 < N and maze[(i + 1, j)] == 0:
                    i += 1
                elif j + 1 < M and maze[(i, j + 1)] == 0:
                    j += 1
                else:
                    break
        path.append((i, j))
        maze[(i, j)] = 2

    return maze, path

def add_obstacles(maze, min_obstacles, N, M):
    obstacles_added = 0
    while obstacles_added < min_obstacles:
        i = random.randint(0, N-1)
        j = random.randint(0, M-1)
        if maze[(i, j)] == 0: 
            maze[(i, j)] = 1
            obstacles_added += 1 #放置障礙直到obstacles_added < min_obstacles
    return

def set_obstacle(maze, N, M):
    while True:
        try:
            c = input("Enter the coordinate to set an obstacle (i,j):")
            c = c.split(",")
            i = int(c[0]) # row
            j = int(c[1]) # col
            if (i, j) in maze:
                if maze[(i, j)] == 2: # path
                    print("Obstacles cannot be placed on the path.")
                elif maze[(i, j)] == 1: # obstacles
                    print("Obstacles already exists at this location.")
                else: # 其他空白的地方
                    maze[(i, j)] = 1
                    print(f"Obstacle placed at {i, j}")
                    break
            else:
                print("KeyError in set_obstacle function. Invaild coordinates. Please input coordinates within the range.")
        except IndexError:
            print("ValueError in set_obstacle function. Need to be coordinates.")
        except ValueError:
            print("ValueError in set_obstacle function. Need to be coordinates.")
        except KeyError:
            print("KeyError in set_obstacle function. Invaild coordinates. Please input coordinates within the range.")

def remove_obstacle(maze, N, M):
    while True:
        try:
            c = input("Enter the coordinate to remove an obstacle (i,j):")
            c = c.split(",")
            i = int(c[0])
            j = int(c[1])
            if (i, j) in maze:
                if maze[(i, j)] == 1: # 原本是障礙的地方可以移除障礙
                    maze[(i, j)] = 0
                    print(f"Obstacle removed at {i, j}")
                    break
                elif maze[(i, j)] == 2: # 障礙不會生成在path上
                    print("Obstacle does not exist on the path.")
                else:
                    print("Obstacle does not exist at this location.")
            else:
                print("KeyError in set_obstacle function. Invaild coordinates. Please input coordinates within the range.")
        except IndexError:
            print("ValueError in remove_obstacle function. Need to be coordinates.")
        except ValueError:
            print("ValueError in remove_obstacle function. Need to be coordinates.")
        except KeyError:
            print("KeyError in set_obstacle function. Invaild coordinates. Please input coordinates within the range.")

def print_maze(maze, N, M):
    try:
        print("+" + "---+" * M)
        for i in range(N):
            row = "|"
            for j in range(M):
                if maze[(i, j)] == 0:
                    row += "   "
                elif maze[(i, j)] == 1:
                    row += " X "
                elif maze[(i, j)] == 2:
                    row += " O "
                row += "|"
            print(row)
            print("+" + "---+" * M)
    except KeyError:
        print("Error: Invalid cell while printing.")

def main():
    while True:
        try:
            file =input("Enter file name:")
            maze, N, M = parse_maze_file(file)
            print_maze(maze, N, M) # 在輸入file之後印出file的地圖
            break  # Exit the loop if file is successfully parsed
        except IOError:
            print("IOError occurred. File not found. Please enter a valid file name.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    m = (M - 1) * (N - 1)
    while True:
        try:
            min_obstacles = int(input(f"Enter the minimum number of obstacles (0-{m}): "))
            if 0 <= min_obstacles <= m:
                break  # Exit the loop if valid input is provided
            else:
                print("ValueError in main function. Invalid number of obstacles.")
        except ValueError:
            print("ValueError in main function. Invalid number of obstacles.1")

    maze, path = generate_path(maze, N, M)
    add_obstacles(maze, min_obstacles, N, M)
    print_maze(maze, N, M)
    
    while True:
        print("Options:")
        print("1. Set obstacle")
        print("2. Remove obstacle")
        print("3. Print maze")
        print("4. Exit")
        choice = input("Enter your option: ")

        if choice == '1':
            set_obstacle(maze, N, M)
        elif choice == '2':
            remove_obstacle(maze, N, M)
        elif choice == '3':
            print_maze(maze, N, M)
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()