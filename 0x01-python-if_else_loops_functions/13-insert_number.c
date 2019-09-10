#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - insert node in a sorted list
 * @head: pointer to list to be add
 * @number: number to add
 * Return: the list with the new number
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *tmp = *head;
/* In case it isn't imput a head*/
	if (head == NULL)
		return (NULL);
/*Allocate the new node*/
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
/*Assign info to the new node*/
	new_node->n = number;
	new_node->next = NULL;
/*Assign the head if the list is empty*/
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	while (tmp->next != NULL)
	{
		if (new_node->n >= tmp->n && new_node->n <= tmp->next->n)
		{
			new_node->next = tmp->next;
			tmp->next = new_node;
			return (new_node);
		}
			tmp = tmp->next;
	}
	return (new_node);
}
