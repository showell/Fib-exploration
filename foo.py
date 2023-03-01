f = dict()
f[1] = 1
f[2] = 1

N = 20
for i in range(1, N+1):
    if i <= 2:
        val = f[i]
    else:
        # Population is sum of two prior generations's populations. But why?
        val = f[i-1] + f[i-2]
    f[i] = val
    print(f"f({i : 3d}) = {val}")

    # garbage collect
    if i - 2 in f:
        del f[i-2]
