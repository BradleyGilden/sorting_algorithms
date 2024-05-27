def cocktail_sort(arr):
    """
        python implentation for cocktail sort
    """
    size = len(arr)
    i = 0
    j = 0
    swapped = True
    while i < size and swapped:
        swapped = False
        # shift biggest to right
        while j < size - i - 1:
            if (arr[j] > arr[j + 1]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
            j += 1

        # shift smallest ot left
        if swapped:
            while j > 0 + i:
                if (arr[j] < arr[j - 1]):
                    swapped = True
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    print(arr)
                j -= 1
        i += 1


if __name__ == "__main__":
    arr = [-94, 64, -97, 29, -22, -17, -31, -57, 79, -60, 91, -10, 54, 54,
           -60, -59, -82, 52, 6, 53]
    cocktail_sort(arr)
    print(arr)
