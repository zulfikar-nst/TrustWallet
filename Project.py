
import itertools

st = ["eager","suspect","improve"]

per = itertools.permutations(st)

for val in per:
        print(*val)
