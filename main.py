
def verification(i, fromm, to):
    if fromm < i < to:
        i = True
        return i
    else:
        return False


def arithmetic(x :int,y :int, z :str):
        if z == "+":
            return (x + y)
        elif z == "-":
            return (x - y)
        elif z == "*":
            return (x * y)
        elif z == "/":
            return (x / y)
        elif z == "**":
            return (x ** y)
        elif z == "%":
            return (x % y)
        elif z == "//":
            return (x // y)
        else:
            return ("Invalid operation")

def palindrom(slovo :str):
    a = '' .join(reversed(slovo))
    if slovo == a:
        print("yes")
    else:
        print("no")

def clear():
    line = input("Line:")
    wrong = input("Wrong symbols:")
    if wrong in line:
        print(line.replace(wrong, ''))






if __name__ == '__main__':
    print(verification(5, 0, 7))
    print(arithmetic(2, 3, '+'))
    print(arithmetic(2, 2, '*'))
    print(arithmetic(4, 2, '-'))
    print(arithmetic(4, 2, '/'))
    print(arithmetic(4, 2, 0))
    print(palindrom('abba'))
    clear()



