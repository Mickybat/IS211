import unittest
import conversions

class Test_conversions(unittest.TestCase):
    def test_k(self):
        self.assertAlmostEqual(conversions.c_to_k(100), 373.15, msg="Testing Kelvin")
        self.assertAlmostEqual(conversions.c_to_k(150), 423.15, msg="Testing Kelvin")
        self.assertAlmostEqual(conversions.c_to_k(200), 473.15, msg="Testing Kelvin")
        self.assertAlmostEqual(conversions.c_to_k(250), 523.15, msg="Testing Kelvin")
        self.assertAlmostEqual(conversions.c_to_k(300), 573.15, msg="Testing Kelvin")

    def test_f(self):
        self.assertAlmostEqual(conversions.c_to_f(100), 212, msg="Testing Fahrenheit")
        self.assertAlmostEqual(conversions.c_to_f(150), 302, msg="Testing Fahrenheit")
        self.assertAlmostEqual(conversions.c_to_f(200), 392, msg="Testing Fahrenheit")
        self.assertAlmostEqual(conversions.c_to_f(250), 482, msg="Testing Fahrenheit")
        self.assertAlmostEqual(conversions.c_to_f(300), 572, msg="Testing Fahrenheit")

    def test_c(self):
        self.assertAlmostEqual(conversions.f_to_c(50), 10, msg="Testing Celsius")
        self.assertAlmostEqual(conversions.f_to_c(60), 15.555555555555555, msg="Testing Celsius")
        self.assertAlmostEqual(conversions.f_to_c(70), 21.11111111111111, msg="Testing Celsius")
        self.assertAlmostEqual(conversions.f_to_c(80), 26.666666666666668, msg="Testing Celsius")
        self.assertAlmostEqual(conversions.f_to_c(90), 32.2222222222222, msg="Testing Celsius")

    def test_fk(self):
        self.assertAlmostEqual(conversions.f_to_k(100), 310.92777777777775, msg="Testing Kelvin")
        self.assertAlmostEqual(conversions.f_to_k(150), 338.7055555555555, msg="Testing Kelvin")
        self.assertAlmostEqual(conversions.f_to_k(200), 366.48333333333335, msg="Testing Kelvin")
        self.assertAlmostEqual(conversions.f_to_k(250), 394.26111111111106, msg="Testing Kelvin")
        self.assertAlmostEqual(conversions.f_to_k(300), 422.0388888888889, msg="Testing Kelvin")

    def test_kf(self):
        self.assertAlmostEqual(conversions.k_to_f(100), -279.66999999999996, msg="Testing Fahrenheit")
        self.assertAlmostEqual(conversions.k_to_f(150),  -189.66999999999996, msg="Testing Fahrenheit")
        self.assertAlmostEqual(conversions.k_to_f(200), -99.66999999999996, msg="Testing Fahrenheit")
        self.assertAlmostEqual(conversions.k_to_f(250), -9.669999999999959, msg="Testing Fahrenheit")
        self.assertAlmostEqual(conversions.k_to_f(300),  80.33000000000004, msg="Testing Fahrenheit")

    def test_kc(self):
        self.assertAlmostEqual(conversions.k_to_c(100),  -173.14999999999998, msg="Testing for Celsius")
        self.assertAlmostEqual(conversions.k_to_c(150),  -123.14999999999998, msg="Testing for Celsius")
        self.assertAlmostEqual(conversions.k_to_c(200), -73.14999999999998, msg="Testing for Celsius")
        self.assertAlmostEqual(conversions.k_to_c(250), -23.14999999999997, msg="Testing for Celsius")
        self.assertAlmostEqual(conversions.k_to_c(300), 26.850000000000023, msg="Testing for Celsius")


if __name__ == '__main__':
    unittest.main()
