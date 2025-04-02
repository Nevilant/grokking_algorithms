import unittest

from introduction_to_algorithms.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_element_found(self):
        """Тестируем случаи, когда элемент присутствует в массиве"""
        # Элемент в середине
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 5), 2)
        # Элемент в начале
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 1), 0)
        # Элемент в конце
        self.assertEqual(binary_search([1, 3, 5, 7, 9], 9), 4)
        # Большой массив
        self.assertEqual(binary_search(list(range(1000)), 500), 500)

    def test_element_not_found(self):
        """Тестируем случаи, когда элемент отсутствует в массиве"""
        # Пустой массив
        self.assertIsNone(binary_search([], 1))
        # Элемент больше всех
        self.assertIsNone(binary_search([1, 3, 5, 7, 9], 11))
        # Элемент меньше всех
        self.assertIsNone(binary_search([1, 3, 5, 7, 9], 0))
        # Элемент между значениями
        self.assertIsNone(binary_search([1, 3, 5, 7, 9], 4))

    def test_single_element(self):
        """Тестируем массив из одного элемента"""
        # Элемент найден
        self.assertEqual(binary_search([42], 42), 0)
        # Элемент не найден
        self.assertIsNone(binary_search([42], 100))

    def test_duplicate_elements(self):
        """Тестируем массив с дубликатами (должен вернуть любой из подходящих индексов)"""
        result = binary_search([1, 2, 2, 2, 3], 2)
        self.assertIn(result, [1, 2, 3])  # Может вернуть любой из индексов 2

    def test_even_length_array(self):
        """Тестируем массив с чётным количеством элементов"""
        self.assertEqual(binary_search([1, 2, 3, 4], 3), 2)
        self.assertEqual(binary_search([1, 2, 3, 4], 1), 0)
        self.assertIsNone(binary_search([1, 2, 3, 4], 5))
