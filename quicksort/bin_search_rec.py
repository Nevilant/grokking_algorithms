def bin_search_rec(arr, value):
    if len(arr) == 0:
        return None

    mid = len(arr) // 2

    if arr[mid] == value:
        return mid
    elif arr[mid] > value:
        return bin_search_rec(arr[:mid], value)
    else:
        rec_resp = bin_search_rec(arr[mid+1:], value)
        return (
            (mid + 1) + rec_resp
            if rec_resp is not None
            else rec_resp
                )


print(bin_search_rec([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))
