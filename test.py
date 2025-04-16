from collections import Counter

lst = Counter(list(input().split(",")))
for k, v in sorted(lst.items()):
    print(f"{k}: {v}")