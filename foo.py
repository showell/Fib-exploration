(babies, teenagers, mamas) = (1, 0, 0)

for i in range(1, 21):
    val = babies + teenagers + mamas
    print(f"f({i: 3d}) = {val: 5d} females = {babies: 5d} babies + {teenagers: 5d} teenagers + {mamas: 5d} mamas")
    # grow
    (babies, teenagers, mamas) = (0, babies, teenagers + mamas)
    # breed
    (babies, teenagers, mamas) = (mamas, teenagers, mamas)
