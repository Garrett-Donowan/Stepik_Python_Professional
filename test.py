import pickle, sys

with open(input(), mode='rb') as file:
    pickle.load(file)
print(*list(map(str.strip, sys.stdin)))
    