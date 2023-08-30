import re


def increment_string(s):
    # Find the last occurrence of a number in the string
    match = re.search(r'(\d+)$', s)
    if match:
        match_num = match.group(1)
        num_len = len(match_num)
        incremented_num = int(match_num) + 1
        incremented_num_str = str(incremented_num).zfill(num_len)
        return s[:match.start(1)] + incremented_num_str
    if not match:
        return s + "1"
