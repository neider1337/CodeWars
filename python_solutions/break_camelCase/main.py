import re


def solution(s):
    return " ".join(re.findall('[a-z]+|[A-Z][a-z]*', s))
