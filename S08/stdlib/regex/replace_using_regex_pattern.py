import re


text = "12-27-1870 02-19-2012"
#       27/12/1870
pat = r"(\d\d)-(\d\d)-(\d\d\d\d)"
#         \1     \2      \3
rep = r"\2/\1/\3"
new_text = re.sub(pat, rep, text)

print(new_text)
