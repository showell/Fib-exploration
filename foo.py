baby_rabbits = 1
teenage_rabbits = 0
mama_rabbits = 0

N = 20
for i in range(1, N+1):
    total_rabbits = baby_rabbits + teenage_rabbits + mama_rabbits
    print(f"f({i : 3d}) = {total_rabbits}")
    (baby_rabbits, teenage_rabbits, mama_rabbits) = (teenage_rabbits + mama_rabbits, baby_rabbits, teenage_rabbits + mama_rabbits)
