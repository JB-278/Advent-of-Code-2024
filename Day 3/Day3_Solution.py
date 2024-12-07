# Import libraries
import re 


input = open("Day 3\\input.txt").read()

# Part 1

input_formatted = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input)

print(input_formatted)

Numbers = []
for line in input_formatted:
    x, y = int(line[0]), int(line[1])
    Multiplied = x*y
    Numbers.append(Multiplied)

Answer1 = sum(Numbers)

print(Answer1)

# Part 2

input_formatted2 = re.sub(r"don't\(\).*?(?:$|do\(\))", '', input, flags=re.DOTALL)

print(input_formatted2)

input_formatted3 = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', input_formatted2)

print(input_formatted3)

Numbers2 = []
for line in input_formatted3:
    x, y = int(line[0]), int(line[1])
    Multiplied = x*y
    Numbers2.append(Multiplied)

Answer2 = sum(Numbers2)

print(Answer2)