

# Give each point in wordsearch a coord e.g. (0,1), (23,54)...etc

# Search each letter
# Then search around that letter for MAS
# If found all 4 then add 1 to Answer

# Looks like something similar to last year Day 3

input = open("Day 4\\input.txt").readlines()

# Part 1

Height, Width = len(input), len(input[0])-1

print(Height)
print(Width)

wordsearch = {(h, w): input[h][w] for h in range(Height) for w in range(Width)}

print(wordsearch)

target = 'XMAS'

Answer1 = 0

directions = [(dh, dw) for dh in [-1, 0, 1] for dw in [-1, 0, 1] if (dh != 0 or dw != 0)]

print(directions)

for h, w in wordsearch:
    for dh, dw in directions:
        x = "".join(wordsearch.get((h + dh * i, w + dw * i), "") for i in range(len(target)))
        Answer1 += x == target

print(Answer1)

# Part 2

# Look for A
# Search in a slash line from A for M and S BOTH DIRECTIONS NEED TO BE THERE
Answer2 = 0
for h, w in wordsearch:
    if wordsearch[h,w] == 'A':
        fs = wordsearch.get((h-1,w-1),"") + wordsearch.get((h+1,w+1),"")
        bs = wordsearch.get((h+1,w-1),"") + wordsearch.get((h-1,w+1),"")
        Answer2 += {fs, bs} <= {"MS", "SM"}

print(Answer2)