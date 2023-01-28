# 3 0 8 1 3 3 ans-->103338
# 9 4 6 2 ans-->2469
input = list(map(int,input().split(' ')))
ans = 0

for i in range(len(input)):
  ans = ans + max(input) * (10**i)
  input.remove(max(input))
  if len(input) == 2 and min(input) == 0:
    i += 2
    ans = ans + max(input) * (10**i)
    break

print(ans)