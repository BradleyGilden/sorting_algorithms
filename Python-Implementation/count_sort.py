def count_sort(arr):
    """
        sorts an array of ints using shell sort
    """
    size = len(arr)
    # determine size of count array
    c_size = max(arr)

    count_array = [0 for _ in range(c_size + 1)]

    # count numbers
    for i in range(size):
        count_array[arr[i]] += 1

    # accumalte the count
    for i in range(1, c_size + 1):
        count_array[i] += count_array[i - 1]

    copy = arr[:]
    # use cumalitive count array to sort
    for i in range(size - 1, -1, -1):
        # decrement value in count array (since original array index starts at
        # 0)
        count_idx = copy[i]
        # print(count_idx, count_array[count_idx])
        arr[count_array[count_idx] - 1] = copy[i]
        count_array[count_idx] -= 1


if __name__ == "__main__":
    arr = [6, 1, 5, 2, 2, 3, 4, 6, 2, 0, 3, 0, 7, 2, 1, 7, 2, 7, 5, 3]
    count_sort(arr)
    print(arr)
