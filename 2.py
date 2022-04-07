import random
import numpy as np

a=["1","2","3"]
b=[4,5,6]

c = list(map(int, a))

d = np.array(c)
e = np.array(b)

f = np.linalg.norm(d[1:]-e[1:])


b = []
for i in range(3):
    a = []
    for j in range(2):
        a.append(random.randint(1,100))
    b.append(a)
print(b)
b = np.array(b)
b = b[np.lexsort(b.T)]
print(b)
print(type(b))
print(len(b))
b = np.delete(b, 2, 0)
print(b)
b = b.tolist()
b.append([1,2])
print(type(b))

print(b)
b.pop()
print(b)