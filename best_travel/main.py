import itertools

def choose_best_sum(t, k, ls):
    best_sum = 0
    for comb in itertools.combinations(ls, k):
        if sum(comb) <= t and sum(comb) > best_sum:
            best_sum = sum(comb)
    if best_sum == 0:
        return None
    if best_sum > 0:
        return best_sum