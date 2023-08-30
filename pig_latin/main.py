def pig_it(text):
    new_text = text.strip()
    if len(new_text)>0 and ' ' in new_text:
        words = ' '.join([word[1:] + word[:1] + "ay" if word.isalpha() else word for word in text.split(' ')])
        return words