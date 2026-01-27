testcases = int(input("").strip())
cases = []

for x in range(testcases):
    line = input("").strip()
    cases.append(line)

for i in cases:
    a = 0
    b = 7
    word = ""
    while b <= len(i):
        focus = i[a:b]
        binary = ""
        for char in focus:
            if char == 'G' or char == 'C': binary += '1'
            else: binary += '0'
        a += 7
        b += 7
        letter = chr(int(binary, 2))
        word += letter
    print(word)    