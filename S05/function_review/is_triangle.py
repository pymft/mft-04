import math

def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False


def extract_line_data(line):
    a, b, c = line.split(',')
    a = int(a)
    b = int(b)
    c = int(c)
    return a, b, c

def detect_type_of_triangle(a, b, c):
    # /Isosceles Equilateral
    sides = [a, b, c]
    sides.sort()

    var = len(set(sides))
    out = []
    if var == 1:
        out.append("Equilateral")
    elif var == 2:
        out.append("Isosceles")

    if math.isclose(sides[-1] ** 2 , (sides[0] ** 2 + sides[1]**2)):
        out.append("Right")

    return out


def read_input_file(fname):
    f = open(fname, mode='r')
    text = f.read()
    lines = text.split('\n')
    return lines


def generate_report(fname, data):
    """

    :param fname:
    :param data:
    :return:
    """
    fw = open(fname, 'w')
    fw.write("number of triangles = ")
    fw.write(str(data['count']))
    fw.write("\nEquilateral = " + str(data["Equilateral"]))
    fw.write("\nRight = " + str(data["Right"]))
    fw.write("\nIsosceles = " + str(data["Isosceles"]))
    fw.close()


lines = read_input_file('input.txt')
report = {'count': 0, 'Equilateral': 0, 'Right': 0, 'Isosceles': 0}

for line in lines:
    a, b, c = extract_line_data(line)
    if is_triangle(a, b, c):
        for t in detect_type_of_triangle(a,b,c):
            report[t] += 1
        report['count'] += 1

print(report)
generate_report('output.txt', report)
