rabbit_pairs = [0]

for i in range(9):
    print(f"{len(rabbit_pairs): 3d}", rabbit_pairs)
    # grow
    rabbit_pairs = [age + 1 for age in rabbit_pairs]

    # breed
    baby_pairs = [0 for age in rabbit_pairs if age >= 2]
    rabbit_pairs = rabbit_pairs + baby_pairs
