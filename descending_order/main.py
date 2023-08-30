def descending_order(num):
    return int("".join(map(str, sorted([i for i in str(num)], reverse=True))))


print(descending_order(0), 0)
print(descending_order(15), 51)
print(descending_order(123456789), 987654321)