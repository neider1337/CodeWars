from collections import Counter


def duplicate_count(text):
    if len(text.strip()) > 0:
        c = dict(Counter(text.lower()))
        filtered_dict = {key: value for key, value in c.items() if value > 1}
        return len(filtered_dict)
    else:
        return 0
