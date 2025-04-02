def recursive_sum(arr):
    if arr == []:
        return 0
    else:
        return recursive_sum(arr[1:]) + arr[0]


print(recursive_sum([1, 2, 3, 4, 5]))
