import re

text = """
user@domain.com
my_email@yahoo.com
whatever@some_domain.net
"""

pat = r"(\w+)@(\w+)\.(\w+)"

res = re.findall(pat, text)
print(res)
