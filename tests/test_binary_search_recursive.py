import unittest

from recursion.binary_search_recursive import binary_search


class TestBinarySearchRecursive(unittest.TestCase):
    def test_element_found(self):
        # Элемент в середине
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)
        # Элемент в начале
        self.assertEqual(binary_search([10, 20, 30], 10), 0)
        # Элемент в конце
        self.assertEqual(binary_search([10, 20, 30], 30), 2)
        # Большой массив
        self.assertEqual(binary_search(list(range(1, 100)), 50), 49)

    def test_element_not_found(self):
        # Элемента нет
        self.assertIsNone(binary_search([1, 2, 3], 4))
        # Пустой массив
        self.assertIsNone(binary_search([], 1))
        # Искомый элемент больше всех
        self.assertIsNone(binary_search([10, 20, 30], 40))
        # Искомый элемент меньше всех
        self.assertIsNone(binary_search([10, 20, 30], 5))

    def test_single_element(self):
        # Массив из одного элемента (нашёлся)
        self.assertEqual(binary_search([42], 42), 0)
        # Массив из одного элемента (не нашёлся)
        self.assertIsNone(binary_search([42], 100))
