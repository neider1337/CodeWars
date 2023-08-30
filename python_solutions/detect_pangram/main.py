from collections import Counter


def is_pangram(s):
    z = "The quick brown fox jumps over the lazy dog".lower().replace(' ', '')
    res = Counter(z)
    comparison = {}
    for char in s:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in comparison:
                comparison[lower_char] += 1
            if lower_char not in comparison:
                comparison[lower_char] = 1
    keys_1 = list(comparison.keys())
    keys_2 = list(res.keys())
    keys_1.sort()
    keys_2.sort()
    if keys_1 == keys_2:
        return True
    else:
        return False


print(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)
