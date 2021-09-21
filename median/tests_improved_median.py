import unittest
import hw_median


class MedianTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(hw_median.improved_median(1, 2, 3), 2)

    def test_2(self):
        self.assertEqual(hw_median.improved_median(4, 2, 10), 4)

    def test_3(self):
        self.assertEqual(hw_median.improved_median(2, 5, 5), 5)

    def test_4(self):
        self.assertEqual(hw_median.improved_median(8, 4, 1), 4)

    def test_5(self):
        self.assertEqual(hw_median.improved_median(1, 3, 2), 2)

    def test_6(self):
        self.assertEqual(hw_median.improved_median(3, 1, 2), 2)

    def test_7(self):
        self.assertEqual(hw_median.improved_median(2, 1, 3), 2)

    def test_8(self):
        self.assertEqual(hw_median.improved_median(1, 3, 2), 2)

    def test_9(self):
        self.assertEqual(hw_median.improved_median(2, 3, 1), 2)

    def test_10(self):
        self.assertEqual(hw_median.improved_median(-1, -3, 0), -1)

    def test_11(self):
        self.assertEqual(hw_median.improved_median(5, 3, 5), 5)

    def test_12(self):
        self.assertEqual(hw_median.improved_median(0.21, 0.11, 0.12), 0.12)


if __name__ == '__main__':
    unittest.main()
