a = 1
b = 0

N = 20
for i in range(1, N+1):
    (a, b) = (b, a + b)
    print(f"f({i : 3d}) = {b}")
