alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Testcase:
    def __init__(self, n_canidates, ballots):
        self.n_canidates = n_canidates
        self.ballots = ballots
    def calculateVotes(self):
        min = "A"
        for k in ballots:
            votes[k[0]] += 1
            if votes[k[0]] < min:
                hello = 1

cases = []

n_testcases = int(input("").strip())

for i in range(n_testcases):
    line = (input("").strip()).split()
    n_ballots = line[0]
    ballots = []
    for j in range(n_ballots):
        ballots.append(input("").strip())
    case = Testcase(line[1], ballots)
    cases.append(case)

for testcase in cases:
    votes = {}
    n_canidates = testcase.n_canidates
    canidates = alphabet[:n_canidates]
    ballots = testcase.ballots
    for letter in canidates:
        votes[letter] = 0
    

