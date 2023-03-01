def grow(pairs):
    return [age + 1 for age in pairs]

def breed(pairs):
    children = [0 for age in pairs if age >= 2]
    return pairs + children

def next_gen(pairs):
    return breed(grow(pairs))

rabbit_pairs = [0]

for i in range(20):
    print(len(rabbit_pairs))
    rabbit_pairs = next_gen(rabbit_pairs)
