"""PART NUMBER 1- IMPLEMENT THE FIBONNACI SEQUENCE"""


def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)


print(fibonnaci(15))

"""PART 2- IMPLEMENT EUCLID'S GCD ALGORITHM"""


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


a = 500
b = 50

print("gcd(", a, ",", b, ") = ", gcd(a, b))

"""PART 3- STRING COMPARISON"""


def compareTo(s1, s2):
    if len(str(s1)) > len(str(s2)):
        return 1
    if len(str(s1)) < len(str(s2)):
        return -1
    else:
        compareTo(len(str(s1)) == len(str(s2)), len(str(s1)))
        return 0


s1 = 'conversation'
s2 = 'talking'
print(compareTo(s1, s2))

