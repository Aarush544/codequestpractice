class Testcase:
    def __init__(self, old_files, new_files):
        self.old_files = old_files
        self.new_files = new_files

class Person:
    def __init__(self, phone_number, address):
        self.phone_number = phone_number
        self.address = address
        
    
amount_of_testcases = int(input("").strip())
testcases = []

for i in range(amount_of_testcases):
    line = input("").strip()
    o = int(line.split()[0])
    n = int(line.split()[1])
    old_files = {}
    for line_num in range(o):
        info = (input("").strip()).split(',')
        person = Person(info[1], info[2])
        old_files[info[0]] = person
    new_files = {}
    for line_num in range(n):
        info = (input("").strip()).split(',')
        person = Person(info[1], info[2])
        new_files[info[0]] = person
    testcases.append(Testcase(old_files, new_files))
    del o
    del n
    del line

output = []

for case in testcases:
    new_files = case.new_files
    old_files = case.old_files
    new = new_files.keys()
    old = old_files.keys()
    combined = old + new
    differences = [x for x in combined if combined.count(x) == 1]

    del old
    del combined

    output = {}
    
    for employee in differences:
        if employee in new:
            output[employee] = "CREATED"
            new.remove(employee)
        else:
            output[employee] = "DELETED"
            old.remove(employee)
    for employee in new: 
        if new_files[employee].phone_number != old_files[employee].phone_number and new_files[employee].address != old_files[employee].address:
            output[employee] = "UPDATED BOTH"
        elif new_files[employee].phone_number != old_files[employee].phone_number:
            output[employee] = "UPDATED PHONE NUMBER"
        elif new_files[employee].address != old_files[employee].address:
            output[employee] = "UPDATED ADDRESS"
    
    output_list = sorted(output.keys())
    
    for i in output_list:
        print(f"{i} {output[i]}")


            



        