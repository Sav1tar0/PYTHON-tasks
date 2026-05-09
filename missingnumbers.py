def missing_numbers_in_range(arr, N):
    full_set = set(range(1, N + 1))
    arr_set = set(arr)
    missing_numbers = list(full_set - arr_set)
    missing_numbers.sort()   
    return missing_numbers
print(missing_numbers_in_range([1, 2, 4, 6], 7))  