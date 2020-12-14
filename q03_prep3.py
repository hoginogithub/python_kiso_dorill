l = [{'A':1}, {'B':2}, {'C': 3}]
print(l)
m = [(list(x.keys())[0], list(x.values())[0]) for x in l]
print({x[0]:x[1] for x in m})