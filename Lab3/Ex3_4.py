def function(str):
    dict = {}
    for i in str:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict
#   return {i:str.count(i) for i in str}

print(function("asdsadsadsa"))