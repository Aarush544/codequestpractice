testcases = int(input("").strip())

people = []

for case in range(testcases):
    line = input("").strip()
    people.append(line)
    
    
for i in people:
    hours_list = i.split(',')
    name = hours_list[0]
    hours_list.pop(0)
    total_hours = 0
    total_minutes = 0
    for day in hours_list:
        hours_minutes = day.split(':')
        hour = int(hours_minutes[0])
        minutes = int(hours_minutes[1])
        total_hours += hour
        total_minutes += minutes
        if total_minutes >= 60:
            total_hours += 1
            total_minutes -= 60
    if total_hours == 1: hour_plurality = "hour"
    else: hour_plurality = "hours"

    if total_minutes == 1: minute_plurality = "minute"
    else: minute_plurality = "minutes"

    print(f"{name}={total_hours} {hour_plurality} {total_minutes} {minute_plurality}")
            

