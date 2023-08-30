def longest_consec(strarr, k):
    if len(strarr) > 0 and len(strarr) >= k > 0:
        longest = ""
        for start in range(len(strarr) - k + 1):
            current_concatenation = ''.join(strarr[start:start + k])
            if len(current_concatenation) > len(longest):
                longest = current_concatenation

        return longest

    return ""