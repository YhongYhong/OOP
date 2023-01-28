def count_char_in_string(x,s):
  d = [letter.count(s) for letter in x]
  return d

print(count_char_in_string(['abba','babana','ann'],'a'))