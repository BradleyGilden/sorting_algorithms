#include <stdio.h>
#include <stdlib.h>
#include "../sort.h"

void insertion_sort_array(int *array, size_t size)
{
	size_t i, j;
	int temp;

	for (i = 1; i < size; i++)
	{
		for(j = i; j > 0 && array[j - 1] > array[j]; j--)
		{
			temp = array[j];
			array[j] = array[j - 1];
			array[j - 1] = temp;
			print_array(array, size);
		}
	}
}

/**
 * create_listint - Creates a doubly linked list from an array of integers
 *
 * @array: Array to convert to a doubly linked list
 * @size: Size of the array
 *
 * Return: Pointer to the first element of the created list. NULL on failure
 */
listint_t *create_listint(const int *array, size_t size)
{
	listint_t *list;
	listint_t *node;
	int *tmp;

	list = NULL;
	while (size--)
	{
		node = malloc(sizeof(*node));
		if (!node)
			return (NULL);
		tmp = (int *)&node->n;
		*tmp = array[size];
		node->next = list;
		node->prev = NULL;
		list = node;
		if (list->next)
			list->next->prev = list;
	}
	return (list);
}

/**
 * main - Entry point
 *
 * Return: Always 0
 */
int main(void)
{
	listint_t *list;
	int array[] = {7, 13, 19, 71, 48, 52, 96, 73, 86, 99};
	size_t n = sizeof(array) / sizeof(array[0]);

	/*print_array(array, n);
	printf("\n");
	insertion_sort_array(array, n);
	printf("\n");
	print_array(array, n); */

	list = create_listint(array, n);
	if (!list)
		return (1);
	print_list(list);
	printf("\n");
	insertion_sort_list(&list);
	printf("\n");
	print_list(list);
	return (0);
}
