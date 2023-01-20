def only_english(string1):
  ans = ''
  newlist = [i for i in string1 if i.isalpha()]
  ans = ans.join(newlist)
  return ans

print(only_english("a[ld[[aslda["))