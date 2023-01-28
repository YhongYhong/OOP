input = {3:4, 5:6, 7:8}

def is_plusone_dictionary(d):
  if sum(d.values()) - sum(d.keys()) == len(d) and min(d.keys())+(len(d)-1)*2 == max(d.keys()) :
    return True
  else: return False

print(is_plusone_dictionary(input))