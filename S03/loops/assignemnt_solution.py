pattern = "*"
ws_pattern = " "
number_of_lines = 10

# part 3
# print(number_of_lines*ws_pattern + pattern)
# for i in range(1, number_of_lines):
#     white_space = ws_pattern * (number_of_lines - i)
#     # asterisks = pattern * (2 * i + 1)
#     middle_ws = ws_pattern * (2 * i - 1)
#     line = white_space + pattern + middle_ws + pattern
#     print(line)
#
# print((2*number_of_lines+1)*pattern)

width = number_of_lines * 2 - 1
for i in range(number_of_lines):
    asterisks = pattern * (2 * i + 1)
    line = asterisks.center(width)
    print(line)
