def count_minus(str):
  input = str.split(' ')
  ans = [i for i in input if i < '0']
  return len(ans)


print(count_minus('3 6 9 -12'))