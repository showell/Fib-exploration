f = dict()
f[1] = 1
f[2] = 1
f[3] = 2

N = 10000
for i in range(1, N+1):
    if i <= 3:
        val = f[i]
    else:
        # More than double the population from two months ago.
        val = 2 * f[i-2] + f[i-3]
    f[i] = val

    if i >= 3:
        assert f[i] == f[i-1] + f[i-2]

    if i >= 4:
        assert f[i-1] + f[i-2] == 2 * f[i-2] + f[i-3]

    # garbage collect
    if i - 3 in f:
        del f[i-3]

print(f"Identities hold up to N={N}")
