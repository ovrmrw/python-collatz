from src.collatz import collatz
import unittest


class CollatzTest(unittest.TestCase):
    def test_collatz(self):
        expected = [5, 16, 8, 4, 2, 1]
        actual = collatz(10)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
