f = dict()
f[1] = 1
f[2] = 1
f[3] = 2

for i in range(1, 21):
    if i <= 3:
        val = f[i]
    else:
        val = 2 * f[i-2] + f[i-3]
    f[i] = val

    print(f"f({i: 3d}) = {val: 5d}")
