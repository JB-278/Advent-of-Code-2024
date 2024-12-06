# Loading inputs

input = open("Day 1\\input.txt")

input_formatted = input.read().strip().split("\n")

# Part 1

left = []
right = []

for thing in input_formatted:
    lefty,righty = thing.split()
    lefty,righty = int(lefty), int(righty)
    left.append(lefty)
    right.append(righty)

left = sorted(left)
right = sorted(right)

Answer1 = 0

for l,r in zip(left,right):
    Answer1 += abs(l-r)

print(Answer1)

# Part 2

Answer2 = 0

for l in left:
    Answer2 += l * right.count(l)

print(Answer2)