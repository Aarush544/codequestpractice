import sys

class Task:
    def __init__(self, name, priority, time_constraint, cycles_needed):
        self.name = name
        self.priority = priority
        self.time_constraint = time_constraint
        self.cycles_needed = cycles_needed

def calculate_order():
    print("HEllo")
    current_cycle = 1
    global task_order
    task_order = []
    while current_cycle <= cycles:
        available_tasks = []

        for i in tasks:
            if i.time_constraint <= current_cycle:
                available_tasks.append(i)

        if not available_tasks:
            task_order.append(f"{current_cycle},Wait")
        else:
            max_prio = 0
            highest = 0

            for i in available_tasks:
                if i.priority > max_prio:
                    max_prio = i.priority
                    highest = i

            task_order.append(f"{current_cycle},{highest.name}")
            highest.cycles_needed -= 1
            if highest.cycles_needed == 0:
                tasks.remove(highest)
        current_cycle += 1




testcases = int(sys.stdin.readline().strip())

current_testcase = 1

while current_testcase <= testcases:
    print("hello")
    line = sys.stdin.readline().strip()
    cycles = int(line.split(",")[0])
    t = int(line.split(",")[1])
    tasks = []
    for i in range(t): 
        task_being_read = sys.stdin.readline().strip()
        attributes = (task_being_read.strip()).split(',')
        task = Task(attributes[0], int(attributes[1]), int(attributes[2]), int(attributes[3]))
        tasks.append(task)
    calculate_order()
    for i in task_order:
        print(i)
    current_testcase += 1