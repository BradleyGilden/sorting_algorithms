def count_sort(arr, place):
    """
        sorts an array of ints using count sort
    """
    # determine size of count array
    size = len(arr)
    count_array = [0 for i in range(10)]

    # count numbers
    for i in range(size):
        count_array[num_at_index(arr[i], place)] += 1

    # accumalte the count
    for i in range(10):
        count_array[i] += count_array[i - 1]
    copy = arr[:]
    # use cumalitive count array to sort
    for i in range(size - 1, -1, -1):
        # decrement value in count array (since original array index starts at
        # 0)
        count_idx = num_at_index(copy[i], place)
        # print(count_idx, count_array[count_idx])
        arr[count_array[count_idx] - 1] = copy[i]
        count_array[count_idx] -= 1


def num_at_index(num, place):
    "finds number at index starting from 1 at the right"
    modulator = pow(10, place)
    divider = modulator / 10

    return int((num % modulator) // divider)


def radix_sort(arr):
    # find max number of digits in a number
    maxl = max([len(str(i)) for i in arr])

    for i in range(1, maxl + 1):
        count_sort(arr, i)


if __name__ == "__main__":
    arr = [632, 31, 55, 2, 3522, 343, 34, 6, 552, 50, 3, 0, 3347, 253, 41, 7,
           64, 7, 75, 3]
    radix_sort(arr)
    print(arr)
