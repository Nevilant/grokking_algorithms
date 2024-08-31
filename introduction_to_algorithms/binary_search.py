def binary_search(array: list, value: int):
    low: int = 0  # Начальный индекс массива
    high: int = len(array) - 1  # Конечный индекс массива

    while low <= high:  # Пока low меньше или равно high (пока не станет 0)
        mid: int = (low + high) // 2  # Получаем средний индекс массива (значение в середине массива)
        guess: int = array[mid]  # Присваиваем переменной guess значение среднего индекса массива
        if guess == value:  # Если guess равно value, то
            return mid  # Возвращаем индекс значения guess
        elif guess > value:  # Если guess больше, чем value, то
            high: int = mid - 1  # Переменной high присваивается значение среднего индекса - 1 (mid - 1)
        else:               # Иначе
            low: int = mid + 1  # Переменной low присваивается значение среднего индекса + 1 (mid + 1)

    return None  # Если не находится такое значение, то возвращаем None


my_list: list = [1, 2, 4, 5, 8, 9, 10, 11, 15]
print(binary_search(my_list, 4))
