from itertools import combinations

transactions = [
    ['milk','bread','butter'],
    ['bread','butter'],
    ['milk','bread'],
    ['milk','butter'],
]

min_support = 2

items = set(item for t in transactions for item in t)

for i in range(1,3):
    print("\nItemset size:",i)
    for combo in combinations(items,i):
        count=sum(1 for t in transactions if set(combo).issubset(t))
        if count>=min_support:
            print(combo,"support:",count)