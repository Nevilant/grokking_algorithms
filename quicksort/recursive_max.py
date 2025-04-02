def recursive_max(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    else:
        max_val = recursive_max(arr[1:])
        return arr[0] if arr[0] > max_val else max_val


print(recursive_max([10, 1, 11, 6]))
