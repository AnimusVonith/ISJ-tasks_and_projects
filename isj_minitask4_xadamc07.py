# minitask 4
mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
wanted = {'a': 17, 'b': 34, 'z': 3}

mcase = {key.lower():(mcase.get(key.lower(), 0)+mcase.get(key.upper(), 0)) for (key, value) in mcase.items()}
print(mcase)