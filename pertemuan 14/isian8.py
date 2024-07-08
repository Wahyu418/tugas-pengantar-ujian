def mystery(n, m):
    p = 0
    e = 0
    while e < n:
        p = m
        e = e + 1
    return p

print(mystery(4, 3))  

n = 4
m = 3
p = 0
e = 0

print(f"Iterasi: 0, p: {p}, e: {e}")
for i in range(1, n + 1):
    p = m
    e = i
    print(f"Iterasi: {i}, p: {p}, e: {e}")
