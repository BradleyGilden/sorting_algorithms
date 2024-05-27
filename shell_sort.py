def shell_sort(arr):
    """
        sorts an array of ints using shell sort
    """
    size = len(arr)
    gap = 1

    while 3 * gap + 1 < size // 2:
        print(gap, 50)
        gap = 3 * gap + 1

    while gap > 0:
        i = gap

        while i < size:
            j = i
            while (j >= gap and arr[j - gap] > arr[j]):
                arr[j - gap], arr[j] = arr[j], arr[j - gap]
                print(gap)
                print(arr)
                j -= gap
            i += gap

        gap = gap // 3


if __name__ == "__main__":
    arr = [60, 53, 60, 94, 69, 75, 91, 81, 50, 76, 49, 95, 4, 6, 87, 22, 34,
           30, 44, 13, 67, 62, 78, 24, 84, 81, 86, 47, 7, 63, 52, 10, 80, 6,
           12, 92, 58, 17, 3, 40, 5, 8, -6, 44, 75, 52, 64, 50, 90, 42]
    shell_sort(arr)
    print(arr)
