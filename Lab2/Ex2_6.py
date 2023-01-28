def add2list(lst1, lst2):
  # ans = []
  # for i in range(len(lst1)):
  #   ans += [lst1[i]+lst2[i]]
  ans = [lst1[i] + lst2[i] for i in range(len(lst1))]
  return ans


print(add2list([9, 8, -10], [-1, -3, 5]))
