(babies, teenagers, mamas) = (1, 0, 0)

for i in range(20):
    print((babies + teenagers + mamas), (babies, teenagers, mamas))
    # grow
    (babies, teenagers, mamas) = (0, babies, teenagers + mamas)
    # breed
    (babies, teenagers, mamas) = (mamas, teenagers, mamas)
