def text_prefix(lst, prefix):
    return [prefix + c for c in lst]


text = "abcde"
for i in range(len(text)):
    char = text[i]
    residue = text[:i] + text[i + 1:]

    res = text_prefix(residue, char)
    print(res)
