def sum_pairs(ints, s):
    seen = {}  # Stores seen values and their indices

    for index, num in enumerate(ints):
        complement = s - num
        if complement in seen:
            return [complement, num]
        seen[num] = index

    return None