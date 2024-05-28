def merge(arr, start, mid, end):
    """merge process"""
    i = start
    j = mid + 1
    copy = []
    # create a second array with ordered elements
    while i <= mid and j <= end:
        if arr[i] > arr[j]:
            copy.append(arr[j])
            j += 1
        else:
            copy.append(arr[i])
            i += 1

    while i <= mid:
        copy.append(arr[i])
        i += 1
    while j <= end:
        copy.append(arr[j])
        j += 1

    # index for the copy
    # replace all the elements in the orignal array with the sorted elements
    j = 0
    for i in range(start, end + 1):
        arr[i] = copy[j]
        j += 1


def merge_sort(arr):
    """
        sorts an array of ints using shell sort
    """
    size = len(arr)
    end = size - 1
    start = 0

    def merge_recursive(arr, start, end):
        if (start < end):
            mid = (start + end) // 2
            merge_recursive(arr, start, mid)
            merge_recursive(arr, mid + 1, end)
            merge(arr, start, mid, end)

    merge_recursive(arr, start, end)


if __name__ == "__main__":
    arr = [60, 53, 60, 94, 69, 75, 91, 81, 50, 76, 49, 95, 4, 6, 87, 22, 34,
           30, 44, 13, 67, 62, 78, 24, 84, 81, 86, 47, 7, 63, 52, 10, 80, 6,
           12, 92, 58, 17, 3, 40, 5, 8, -6, 44, 75, 52, 64, 50, 90, 42]
    merge_sort(arr)
    print(arr)
