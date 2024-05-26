def lomuto_partition(arr, start, end):
    """"""
    i, j = start, start
    pivot = arr[end]

    while j < end:
        if (arr[j] <= pivot):
            if (i != j):
                arr[j], arr[i] = arr[i], arr[j]
            i += 1
        j += 1

    if (i != end):
        arr[i], arr[end] = pivot, arr[i]

    return i


def hoare_partition(arr, start, end):
    mid = (start + end) // 2
    arr[mid], arr[end] = arr[end], arr[mid]

    i = start  # left
    j = end - 1  # right

    while (1):
        while arr[i] < arr[end]:
            i += 1
        while arr[j] > arr[end]:
            j -= 1

        if (j > i):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[i], arr[end] = arr[end], arr[i]

    return i


def quick_sort(arr, hoare=False):
    """
        sorts an array of ints using bubble sort
    """
    size = len(arr)

    def quick_sort_recurse(start=0, end=size-1):
        if start < end:
            if hoare:
                pivot = hoare_partition(arr, start, end)
            else:
                pivot = lomuto_partition(arr, start, end)
            quick_sort_recurse(start, pivot - 1)
            quick_sort_recurse(pivot + 1, end)

    quick_sort_recurse()


if __name__ == "__main__":
    arr = [-94, 64, -97, 29, -22, -17, -31, -57, 79, -60, 91, -10, 54, 54,
           -60, -59, -82, 52, 6, 53]
    quick_sort(arr)
    print("Lomuto")
    print(arr)
    arr = [-94, 64, -97, 29, -22, -17, -31, -57, 79, -60, 91, -10, 54, 54,
           -60, -59, -82, 52, 6, 53]
    quick_sort(arr, True)
    print("Hoare")
    print(arr)
