def text_prefix(lst, prefix):
    return [prefix + c for c in lst]


def fun(text, n):
    if n == 1:
        return list(text)

    out = []
    for i in range(len(text)):
        char = text[i]
        residue = text[:i] + text[i + 1:]
        res = text_prefix(fun(residue, n-1), char)
        out.extend(res)

    return out

print(fun("abcde", 3))