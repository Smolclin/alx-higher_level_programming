#include "lists.h"

/**
 * check_cycle - a function in C that checks if a
 * singly linked list has a cycle in it
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fst, *slw;

	if (!list || !list->next)
		return (0);
	fst = list;
	slw = list;
	
	while (slw != NULL && fst != NULL && fst->next != NULL)
	{
		slw = slw->next;
		fst = fst->next->next;
		if (slw == fst)
		{
			return (1);
		}
	}
	return (0);
}
