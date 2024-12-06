# Loading inputs

input = open("Day 2\\input.txt")

input_formatted = input.read().strip().split("\n")

# Part 1

def SafetyCheck(n):
    # First check if sorted from low>high or high>low
    Sorted = (n==sorted(n) or n==sorted(n,reverse=True))
    # Each number is within 3 of the next
    Safe = True
    for x in range(len(n)-1):
        difference = abs(n[x]-n[x+1])
        if not 1<=difference<=3:
            Safe = False
    return Sorted and Safe

Answer1 = 0

for line in input_formatted:
    x = list(map(int, line.split()))
    if SafetyCheck(x):
        Answer1 += 1

print(Answer1)

# Part 2

# Wtf is this
Answer2 = 0

for line in input_formatted:
    x = list(map(int, line.split()))
    Safe = False
    for y in range(len(x)):
        n = x[:y] + x[y+1:]
        if SafetyCheck(n):
            Safe = True
    if Safe:
        Answer2 += 1


print(Answer2)