def order(sentence):
    # The words in the input String will only contain valid consecutive numbers.
    dict = {}
    if len(str(sentence)) == 0:
        return ""
    if len(str(sentence)) > 0 and ' ' not in sentence.strip():
        return sentence
    if len(str(sentence)) > 0 and ' ' in sentence.strip():
        z = sentence.split(' ')
    for word in z:
        for letter in word:
            if letter.isnumeric():
                dict[letter] = word
    value = ' '.join([value for key, value in sorted(dict.items())])
    return value