import sys

testcases = int(input().strip())
messages = []

for case in range(testcases):
    line = input("").strip()
    messages.append(line.strip())


for message in messages:
    i = 0
    decodedMessage = ""
    while i < len(message) - 1:
        if message[i] in ['a', 'e', 'i', 'o', 'u']:
            i += 1
            decodedMessage += message[i]
        i += 1
    print(decodedMessage)
            

