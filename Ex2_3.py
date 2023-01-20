x = [[1, -3, 2], [-8, 5], [-1, -4, -3]]

def delete_minus(x):
  ans = [[i for i in list if i >= 0] for list in x]
  return ans

print(delete_minus(x))
