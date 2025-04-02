import unittest

from quicksort.loop_sum import summ


class TestLoopSum(unittest.TestCase):
    """Тестируем валидные значения в массиве"""

    def test_positive_value(self):
        # Положительные цифры
        self.assertEqual(summ([1, 2, 3, 4, 5]), 15)
        # Отрицательные числа
        self.assertEqual(summ([-1, -10]), -11)
        # Десятичные числа
        self.assertEqual(summ([-0.01, 0.01, 1.99, 10.01, 99.99, 100.01, -99.99]), 112.01)

    def test_bad_value(self):
        # Пустой массив
        self.assertEqual(summ([]), 0)
