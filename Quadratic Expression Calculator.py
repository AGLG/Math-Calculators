def root_of_quadratic_expression():
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    ac = float(a * c)
    if ac >= 0 and b >= 0:
        num_1 = ac
        num_2 = ac/num_1
        while num_1 + num_2 != b:
            if num_1 == 1:
                print("No solution")
                return [1, 1, 1, 1, 1]
            else:
                num_1 -= 1
                num_2 = ac / num_1
    elif ac > 0 and b < 0:
        num_1 = -1 * ac
        num_2 = ac/num_1
        while num_1 + num_2 != b:
            if num_1 < -1:
                num_1 += 1
                num_2 = ac / num_1
            else:
                print("No solution")
                return [1, 1, 1, 1, 1]
    else:
        num_1 = ac
        num_2 = ac / num_1
        while num_1 + num_2 != b:
            if num_1 < -1:
                num_1 += 1
                num_2 = ac / num_1
            else:
                print("No solution")
                return [1, 1, 1, 1, 1]
    if num_1 % 1 == 0:
        num_1 = int(num_1)
    if a % 1 == 0:
        a = int(a)
    if b % 1 == 0:
        b = int(b)
    if c % 1 == 0:
        c = int(c)
    if num_2 % 1 == 0:
        num_2 = int(num_2)
    print("The roots are " + str(num_1) + ", " + str(num_2))
    return [num_1, num_2, a, b, c]


def has_common_divisor(num_a, num_b):
    if num_a == 0 or num_b == 0:
        return False
    if num_a < 0:
        num_a *= -1
    if num_b < 0:
        num_b *= -1
    if num_a < num_b:
        the_number = num_a
        while the_number != 0:
            if num_a % the_number == 0 and num_b % the_number == 0:
                return True
            the_number -= 1
        return False
    else:
        the_number = num_b
        while the_number != 0:
            if num_a % the_number == 0 and num_b % the_number == 0:
                return True
            the_number -= 1
        return False


def get_largest_common_divisor(num_a, num_b):
    if num_a == 0 or num_b == 0:
        return 1
    if num_a < 0:
        num_a *= -1
    if num_b < 0:
        num_b *= -1
    if num_a < num_b:
        the_number = num_a
        while the_number != 0:
            if num_a % the_number == 0 and num_b % the_number == 0:
                break
            the_number -= 1
    else:
        the_number = num_b
        while the_number != 0:
            if num_a % the_number == 0 and num_b % the_number == 0:
                break
            the_number -= 1
    return the_number


def get_new_expression():
    roots = root_of_quadratic_expression()
    if has_common_divisor(roots[1], roots[2]):
        str_a = str(roots[2]) + "x^2+" + str(roots[1]) + "x+" + str(roots[0]) + "x+" + str(roots[4])
        m = get_largest_common_divisor(roots[1], roots[2])
        str_b = str(m) + "x(" + str(int(roots[2]/m)) + "x+" + str(int(roots[1]/m)) + ")+" + str(int(roots[0]/(roots[2]/m))) + "(" + str(int(roots[2]/m)) + "x+" + str(int(roots[1]/m)) + ")"
        str_c = "(" + str(int(roots[2]/m)) + "x+" + str(int(roots[0]/(roots[2]/m))) + ")(" + str(int(roots[2]/m)) + "x+" + str(int(roots[1]/m)) + ")"
        str_a = str_a.replace("+-", "-")
        str_b = str_b.replace("+-", "-")
        str_c = str_c.replace("+-", "-")
        print(str_a + "\n" + str_b + "\n" + str_c)
    elif has_common_divisor(roots[0], roots[2]):
        str_a = str(roots[2]) + "x^2+" + str(roots[0]) + "x+" + str(roots[1]) + "x+" + str(roots[4])
        m = get_largest_common_divisor(roots[0], roots[2])
        str_b = str(m) + "x(" + str(int(roots[2]/m)) + "x+" + str(int(roots[0]/m)) + ")+" + str(int(roots[1]/(roots[2]/m))) + "(" + str(int(roots[2]/m)) + "x+" + str(int(roots[0]/m)) + ")"
        str_c = "(" + str(int(roots[2]/m)) + "x+" + str(int(roots[1]/(roots[2]/m))) + ")(" + str(int(roots[2]/m)) + "x+" + str(int(roots[0]/m)) + ")"
        str_a = str_a.replace("+-", "-")
        str_b = str_b.replace("+-", "-")
        str_c = str_c.replace("+-", "-")
        print(str_a + "\n" + str_b + "\n" + str_c)
    else:
        str_a = str(roots[2]) + "x^2+" + str(roots[0]) + "x+" + str(roots[1]) + "x+" + str(roots[4])
        str_b = str(roots[2]) + "x(x+" + str(roots[0] / roots[2]) + ")+" + str(roots[1]) + "(x+" + str(roots[0] / roots[2]) + ")"
				str_c = "(" + str(roots[2]) + "x+" + str(roots[1]) + ")(x+" + str(roots[0] / roots[2]) + ")"
        str_a = str_a.replace("+-", "-")
        str_b = str_b.replace("+-", "-")
        str_c = str_c.replace("+-", "-")
        print(str_a + "\n" + str_b + "\n" + str_c)


while True:
    get_new_expression()

"""
def get_new_expression():
    roots = root_of_quadratic_expression()
    if has_common_divisor(roots[1], roots[2]):
        print(str(roots[2]) + "x^2+" + str(roots[1]) + "x+" + str(roots[0]) + "x+" + str(roots[4]))
        m = get_largest_common_divisor(roots[1], roots[2])
        print(str(m) + "x(" + str(int(roots[2]/m)) + "x+" + str(int(roots[1]/m)) + ")+" + str(int(roots[0]/(roots[2]/m))) + "(" + str(int(roots[2]/m)) + "x+" + str(int(roots[1]/m)) + ")")
        print("(" + str(int(roots[2]/m)) + "x+" + str(int(roots[0]/(roots[2]/m))) + ")(" + str(int(roots[2]/m)) + "x+" + str(int(roots[1]/m)) + ")")
    elif has_common_divisor(roots[0], roots[2]):
        print(str(roots[2]) + "x^2+" + str(roots[1]) + "x+" + str(roots[0]) + "x+" + str(roots[4]))
        m = get_largest_common_divisor(roots[1], roots[2])
        print(str(m) + "x(" + str(int(roots[2]/m)) + "x+" + str(int(roots[0]/m)) + ")+" + str(int(roots[1]/(roots[2]/m))) + "(" + str(int(roots[2]/m)) + "x+" + str(int(roots[0]/m)) + ")")
        print("(" + str(int(roots[2]/m)) + "x+" + str(int(roots[1]/(roots[2]/m))) + ")(" + str(int(roots[2]/m)) + "x+" + str(int(roots[0]/m)) + ")")
    else:
        print(str(roots[2]) + "x^2+" + str(roots[0]) + "x+" + str(roots[1]) + "x+" + str(roots[4]))
        print(str(roots[2]) + "x(x+" + str(roots[0] / roots[2]) + ")+" + str(roots[1]) + "(x+" + str(roots[0] / roots[2]) + ")")
        print("(" + str(roots[2]) + "x+" + str(roots[1]) + ")(x+" + str(roots[0] / roots[2]) + ")")
"""
