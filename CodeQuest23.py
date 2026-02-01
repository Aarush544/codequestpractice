class Testcase:
    def __init__(self, height, width, maze_str):
        pass

n_testcases = int(input("").strip())
testcases = []


for i in range(n_testcases):
    line = input("").strip().split()
    height = int(line[0])
    width = int(line[1])
    big_maze = ""
    for line_n in range(height):
        line = input("").strip()
        big_maze += line + '\n'
    big_maze.rstrip()
    case = Testcase(height, width, big_maze)
    print(big_maze)