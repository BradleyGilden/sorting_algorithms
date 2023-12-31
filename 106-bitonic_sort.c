#include "sort.h"

/**
 * bitonic_merge - merges the sequences into a complete sorted array
 * @low: start of split array
 * @len: length of split array
 * @dir: direction of bitonic sequence
 * @arr: array to sort
 * @size: size of the array
 */
void bitonic_merge(int *arr, int low, int len, int dir, size_t size)
{
	int i, temp, k;

	if (len > 1)
	{
		k = len / 2;
		for (i = low; i < low + k; i++)
		{
			if (dir == (arr[i] > arr[i + k]))
			{
				temp = arr[i];
				arr[i] = arr[i + k];
				arr[i + k] = temp;
			}
		}
		bitonic_merge(arr, low, k, dir, size);
		bitonic_merge(arr, low + k, k, dir, size);
	}
}

/**
 * bitonic_split - splits the array down to its modular elements
 * @low: start of split array
 * @len: length of split array
 * @dir: direction of bitonic sequence
 * @arr: array to sort
 * @size: size of the array
 */
void bitonic_split(int *arr, int low, int len, int dir, size_t size)
{
	int k = len / 2;
	char *str = (dir == 1) ? "UP" : "DOWN";

	if (len > 1)
	{
		printf("Merging [%d/%lu] (%s):\n", len, size, str);
		print_array(arr + low, len);

		bitonic_split(arr, low, k, 1, size);
		bitonic_split(arr, low + k, k, 0, size);
		bitonic_merge(arr, low, len, dir, size);

		printf("Result [%d/%lu] (%s):\n", len, size, str);
		print_array(arr + low, len);
	}
}

/**
 * bitonic_sort - function initiates the bitionic sort algorithm
 * @array: array to sort
 * @size: size of the array
 */
void bitonic_sort(int *array, size_t size)
{
	if (array == NULL || size < 2)
		return;

	bitonic_split(array, 0, (int)size, 1, size);
}
