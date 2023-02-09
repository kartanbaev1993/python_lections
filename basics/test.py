dict1 = {'a':{'key':1}, 'b':{'key':2}, 'c':{'key':3}}
res = {}
for key, value in dict1.items():
    res[key] = value['aaa']
print(res)
