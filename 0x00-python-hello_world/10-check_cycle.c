#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The singly linked list to check
 *
 * Return: 1 if has a cycle in it or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle = list, *rabbit = list;
	int num = 0;

	while ((turtle && rabbit) && rabbit->next)
	{
		turtle = turtle->next;

		if (rabbit->next || rabbit->next->next)
			rabbit = rabbit->next->next;
		else
			break;

		if (turtle == rabbit)
		{
			num = 1;
			break;
		}
	}
	return (num);
}
