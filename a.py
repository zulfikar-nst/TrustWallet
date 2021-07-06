import itertools

st = ["a","b","c","d","e","f","g","h"]

per = itertools.permutations(st, 8)

for val in per:
        print(*val)
