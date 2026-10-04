import unittest

import ohms_law


class TestOhmsLaw(unittest.TestCase):
    def test_voltage(self):
        self.assertEqual(ohms_law.voltage(2, 5), 10)

    def test_current(self):
        self.assertEqual(ohms_law.current(10, 5), 2)

    def test_resistance(self):
        self.assertEqual(ohms_law.resistance(10, 2), 5)

    def test_power(self):
        self.assertEqual(ohms_law.power(10, 2), 20)

    def test_zero_resistance(self):
        with self.assertRaises(ValueError):
            ohms_law.current(10, 0)

    def test_zero_current(self):
        with self.assertRaises(ValueError):
            ohms_law.resistance(10, 0)


if __name__ == "__main__":
    unittest.main()
