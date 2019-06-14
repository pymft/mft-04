def no_special_chars(text):
    for c in ";:!-.,?":
        text = text.replace(c, '')
    return text


def unique_words(text: str, ignore_case=False, ignore_punctuation=False):
    if ignore_case:
        text = text.lower()

    if ignore_punctuation:
        text = no_special_chars(text)

    words = text.split()
    uniq = set(words)
    return uniq


text = "Hello hello HELLO hi HI? Hi hi hi hello "
res = unique_words(text, ignore_case=True, ignore_punctuation=True)
print(res)


