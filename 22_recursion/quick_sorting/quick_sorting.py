def quick_sorting(array):
    if not array:
        return array
    pivot = array[len(array) // 2]
    middle, left, right = [], [], []
    for e in array[:pivot] + array[pivot + 1:]:
        if e < pivot:
            left += [e]
        elif e > pivot:
            right += [e]
        else:
            middle += [e]
    return quick_sorting(left) + middle + quick_sorting(right)
