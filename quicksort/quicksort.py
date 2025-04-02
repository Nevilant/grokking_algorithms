def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    low = [x for x in arr[1:] if x < pivot]
    high = [x for x in arr[1:] if x >= pivot]
    return quicksort(low) + [pivot] + quicksort(high)

# def qsort(arr):
#     if len(arr) < 2:
#         return arr
#     else:
#         return quicksort(arr[0] + [arr[1]] + quicksort(arr[]))


print(quicksort([33, 15, 10]))
