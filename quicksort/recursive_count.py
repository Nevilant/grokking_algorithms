def recursive_count(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + recursive_count(arr[1:])


print(recursive_count([1, 2, 3, 4, 5, 6, 7, 8, 9]))
