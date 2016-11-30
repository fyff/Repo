a = [1, 1, 1, 1, 0, 0, 0, 0, 1]
b = sum(a)
a = [0] * (len(a) - b) + [1] * b
print(a)
