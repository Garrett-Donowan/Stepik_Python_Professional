from collections import Counter

lst = Counter(list(input().split(",")))
for k, v in sorted(lst.items()):
    sum_k = [ord(x) for x in k.replace(" ", "")]
    print(sum_k)