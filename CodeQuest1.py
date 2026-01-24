import sys

testcases = int(sys.stdin.readline().strip())
messages = []

for line in sys.stdin:
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
            
