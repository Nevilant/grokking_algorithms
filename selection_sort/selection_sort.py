def find_smallest(arr):  # Функция для поиска наименьшего элемента массива
    smallest = arr[0]  # Для хранения наименьшего значения
    smallest_index = 0  # Для хранения индекса наименьшего значения
    for i in range(1, len(arr)):  # Проходим по массиву
        if arr[i] < smallest:  # Если значение i меньше наименьшего значения
            smallest = arr[i]  # smallest принимает значение arr[i]
            smallest_index = i  # smallest_index принимает значение индекса arr[i]
    return smallest_index  # Возвращает наименьшее значение


def selection_sort(arr):  # Сортировка массива
    new_arr = []  # Создаем новый пустой массив
    copied_arr = list(arr)  # Создаем копию массива arr перед изменением
    for i in range(len(copied_arr)):
        smallest = find_smallest(copied_arr)  # Находит наименьший элемент в массиве и добавляет его в новый массив
        new_arr.append(copied_arr.pop(smallest))  # Добавляем наименьший элемент из массива copied_arr в конец массива new_arr, затем удаляя его из массива copied_arr
    return new_arr
