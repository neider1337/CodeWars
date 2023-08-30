def count_bits(n):
    z = 0
    for n in format(n, 'b'):
        z += int(n)
    return z
