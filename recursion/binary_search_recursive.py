def binary_search(arr, target):  # Бинарный поиск через рекурсию
    if len(arr) == 0:  # Если массив пустой
        return None  # Возвращаем None

    mid = len(arr) // 2  # Получаем средний индекс массива

    if arr[mid] == target:  # Если значение индекса равно искомому
        return mid  # Возвращаем индекс искомого значения
    elif arr[mid] > target:  # Если значение больше искомого
        return binary_search(arr[:mid], target)  # Рекурсивно вызываем функцию binary_search по массиву от 0 до mid
    else:  # Иначе
        recursive_response = binary_search(arr[mid+1:], target)  # Результат рекурсивного вызова сохраняется в переменную recursive_response
        return (
            (mid + 1) + recursive_response
            if recursive_response is not None
            else recursive_response
        )


# print(binary_search([6, 7, 8, 9, 10], 8))
# print(binary_search([6, 7, 8, 9, 10], 6))
