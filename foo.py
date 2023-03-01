def grow(generation_counts):
    return [0] + generation_counts

def breed(generation_counts):
    baby_count = sum(cnt for cnt in generation_counts[2:])
    return [baby_count] + generation_counts[1:]

def compress(generation_counts):
    if len(generation_counts) < 3:
        return generation_counts

    return [generation_counts[0], generation_counts[1],  sum(generation_counts[2:])]

def next_gen(generation_counts):
    return breed(grow(generation_counts))

generation_counts = [1]

for i in range(20):
    generation_counts = compress(generation_counts)
    print(sum(generation_counts), generation_counts)
    generation_counts = next_gen(generation_counts)
