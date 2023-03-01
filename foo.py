a = 1
b = 0
c = 0

N = 20
for i in range(1, N+1):
    d = b + c
    print(f"f({i : 3d}) = {a + d}")
    (a, b, c) = (d, a, d)
