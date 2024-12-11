# Split up the rules and the pages
# Create dictionary of each rule (first) and every corresponding number that goes after (second)

from collections import defaultdict

rules, data = open("Day 5\\data.txt").read().split('\n\n')

print(rules)
print(data)

orders = defaultdict(list)
for x in rules.splitlines():
    first, second = x.split('|')
    orders[int(first)].append(int(second))

print(orders)

update = [list(map(int, line.split(','))) for line in data.splitlines()]

print(update)

Answer1 = 0
Answer2 = 0
for pages in update:
    correct_pages = sorted(pages, key= lambda page: -len([order for order in orders[page] if order in pages]))
    if  pages == correct_pages:
        Answer1 += pages[len(pages) // 2]
    else:
        Answer2 += correct_pages[len(correct_pages) // 2]
print(Answer1)
print(Answer2)