
def type_of_triangle(a, b, c):
    # "متساوی الساقین"
    # متساوی الاضلاع
    # قائم الزاویه
    # هیچ کدام
    # مثلث نیست!

def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False
