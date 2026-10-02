import unittest

from calculadora import dividir, multiplicar, somar, subtrair


class TestCalculadora(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)

    def test_subtrair(self):
        self.assertEqual(subtrair(5, 3), 2)
        self.assertEqual(subtrair(3, 5), -2)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(multiplicar(7, 0), 0)

    def test_dividir(self):
        self.assertEqual(dividir(10, 4), 2.5)

    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            dividir(1, 0)


if __name__ == "__main__":
    unittest.main()
