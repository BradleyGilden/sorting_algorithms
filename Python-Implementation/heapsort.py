def heapify(arr, N, i):
    """heapifies tree at parent i"""
    # left node pos
    left = 2 * i + 1
    # right node pos
    right = 2 * i + 2

    # assume largest number is at parent
    largest = i

    if (left < N and arr[left] > arr[largest]):
        largest = left

    if (right < N and arr[right] > arr[largest]):
        largest = right

    if (largest != i):
        arr[i], arr[largest] = arr[largest], arr[i]
        # heapify again making the l or r node the new parent which previously
        # held the largest number the sub tree
        heapify(arr, N, largest)


def heap_sort(arr):
    """
        sorts an array of ints using heap sort
    """
    N = len(arr)
    # --------------- build max heap --------------------------------
    # why from (n-1)//2? Because we are starting from the last parent node
    # in the tree
    for i in range((N - 1) // 2, -1, -1):
        heapify(arr, N, i)

    # the array will now be semi-sorted as a max heap

    # move biggest elment to the end and heapify array till it's done
    for i in range(N - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [60, 53, 60, 94, 69, 75, 91, 81, 50, 76, 49, 95, 4, 6, 87, 22, 34,
           30, 44, 13, 67, 62, 78, 24, 84, 81, 86, 47, 7, 63, 52, 10, 80, 6,
           12, 92, 58, 17, 3, 40, 5, 8, -6, 44, 75, 52, 64, 50, 90, 42]
    heap_sort(arr)
    print(arr)
