#include "lists.h"
#include <stdio.h>

void reverse(listint_t **head);
int compare_lists(listint_t *head, listint_t *middle, int len);

/**
 * is_palindrome - function in C that checks if a
 * singly linked list is a palindrome
 * @head: pointer to the head pointer
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int len, j;
	listint_t *tmp;
	listint_t *middle;

	if (head == NULL || *head == NULL)
		return (1);
	tmp = *head;
	middle = *head;

	for (len = 0; tmp != NULL; len++)
		tmp = tmp->next;
	len = len / 2;

	for (j = 1; j < len; j++)
		middle = middle->next;
	if (len % 2 != 0 && len != 1)
	{
		middle = middle->next;
		len = len - 1;
	}
	reverse(&middle);
	j = compare_lists(*head, middle, len);

	return (j);
}

/**
 * compare_lists - to compare two lists
 * @head: pointer to the head
 * @middle: pointer to the middle
 * @len: the length of the list
 * Return: 1 if they are the same 0 if not
 */
int compare_lists(listint_t *head, listint_t *middle, int len)
{
	int j;

	if (head == NULL || middle == NULL)
		return (1);
	for (j = 0; j < len; j++)
	{
		if (head->n != middle->n)
			return (0);
		head = head->next;
		middle = middle->next;
	}
	return (1);
}

/**
 * reverse - reverses a list
 * @head: pointer to the head of reverse list
 */
void reverse(listint_t **head)
{
	listint_t *current;
	listint_t *next;
	listint_t *prev;

	if (head == NULL || *head == NULL)
		return;

	prev = NULL;
	current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
