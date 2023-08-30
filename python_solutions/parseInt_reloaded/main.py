def get_first_ten(nr):
    numbers = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
        "ten": 10,
        "eleven": 11,
        "twelve": 12
    }
    for key, value in numbers.items():
        if nr in key:
            return numbers[key]


def get_teens(nr):
    numbers = {
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19
    }
    for key, value in numbers.items():
        if nr in key:
            return numbers[key]


def get_tens(nr):
    numbers = {
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90
    }
    for key, value in numbers.items():
        if nr in key:
            return numbers[key]


def get_big_numbers(nr):
    numbers = {"hundred": 100, "thousand": 1000, "million": 1000000}
    for key, value in numbers.items():
        if nr in key:
            return numbers[key]


# myślniki ogarniete


def parse_int(string):
    z = string.split(" ")
    hundreds = ["hundred", "thousand", "million"]
    temp_index = []
    for element in z:
        if 'and' == element:
            z.pop(z.index(element))
    for index, item in enumerate(z):
        if '-' in item:
            for sub_item in item.split('-'):
                if "ty" in sub_item:
                    temp10 = get_tens(sub_item)
                else:
                    temp1 = get_first_ten(sub_item)
            z[index] = temp10 + temp1
        elif "ty" in item:
            z[index] = get_tens(item)
        elif "teen" in item:
            z[index] = get_teens(item)
        elif item in hundreds:
            z[index] = get_big_numbers(item)
            if z[index] == 100:
                z[index] *= z[index - 1]
                temp_index.insert(0, index - 1)
        else:
            z[index] = get_first_ten(item)

    for i in temp_index:
        z.pop(i)
    if 1000 in z:
        z[z.index(1000) - 1] = sum(z[:z.index(1000)])
        z[-1] = z[z.index(1000) - 1] * z[z.index(1000)] + sum(
            z[z.index(1000) + 1:])
    elif 1000000 in z:
        return z[-1]
    else:
        return sum(z)
    return z[-1]
