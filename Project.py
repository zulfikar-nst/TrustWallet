
import itertools

st = ["eager","suspect","improve","multiply","fabric","victory","injury","pair",>

per = itertools.permutations(st)

for val in per:
        print(*val)
