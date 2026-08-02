def bubble_sort(arr: list) -> list:
    n = len(arr)
    arr_copy = arr.copy()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        if not swapped:
            break
    return arr_copy

# Example Usage
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))