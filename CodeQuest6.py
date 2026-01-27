testcases = int(input("").strip())

class Testcase:
    def __init__(self, n, sensors):
        self.n = n
        self.sensors = sensors



cases = []


for a in range(testcases):
    
    n = int(input("").strip())
    sensor_list = (input("").strip()).split()
    object = Testcase(n, sensor_list)
    cases.append(object)

for case in cases:
    total_sensors = case.n
    sensor_list = case.sensors
    for i in range(1, total_sensors):
        if str(i) not in sensor_list:
            missing_sensor = i
            break
    print(int(missing_sensor))