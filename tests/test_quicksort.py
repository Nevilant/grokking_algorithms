import unittest

from quicksort.quicksort import quicksort


class TestQuickSort(unittest.TestCase):
    """Позитивные тесты"""
    def test_positive_value(self):
        # Один элемент
        self.assertEqual(quicksort([1]), [1])
        # Два элемента
        self.assertEqual(quicksort([2, 1]), [1, 2])
        # Три элемента
        self.assertEqual(quicksort([50, 33, 1]), [1, 33, 50])
        self.assertEqual(quicksort([1, 33, 50]), [1, 33, 50])
        self.assertEqual(quicksort([33, 50, 1]), [1, 33, 50])
        self.assertEqual(quicksort([50, 1, 33]), [1, 33, 50])
        # Четыре элемента
        self.assertEqual(quicksort([50, 33, 1, 7]), [1, 7, 33, 50])
        # Много элементов
        self.assertEqual(quicksort([50, 33, 1, 66, 5, 10, 0.01, -12]), [-12, 0.01, 1, 5, 10, 33, 50, 66])
