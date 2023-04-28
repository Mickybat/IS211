def c_to_k(c):
    return c + 273.15


c = 0
print("Temperature in Kelvin (K) = ", c_to_k(c))


def c_to_f(n):
    return (n*1.8)+32


n = 0
print("Temperature in Fahrenheit (F) = ", c_to_f(n))


def f_to_c(f):
    return(f - 32) * 5 / 9


f = 0
print("Temperature in Celsius (C) = ", f_to_c(f))


def f_to_k(fk):
    return 273.15 + ((fk - 32) * (5/9))


fk = 0
print("Temperature in Kelvin(K) = ", f_to_k(fk))

def k_to_f(kf):
    return 1.8*(kf-273.15) + 32


kf = 0
print("Temperature in Fahrenheit(F) = ", k_to_f(kf))

def k_to_c(kc):
    return kc - 273.15

kc = 0
print("Temperature in Celcius(C)", k_to_c(kc))


