#include "lists.h"
/**
 * check_cycle - check if there is a cycle
 * @list: pointer to list to be analyzed
 * Return: 1 is cycle 0 not
 */
int check_cycle(listint_t *list)
{
	listint_t *tortoise;
	listint_t *hare;

	if (list == NULL || list->next == NULL)/*If the list is null or just 1 node*/
		return (0);

	tortoise = hare = list;/*Start at the same point*/

	while (tortoise && hare && hare->next)
	{
		tortoise = tortoise->next;/*1 step hop*/
		hare = hare->next->next;/*2 steps hop*/
		if (tortoise == hare)
			return (1);
	}
	return (0);
}
