#include "lists.h"

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: head of linked list
 * @number: number
 * Return: address of new node; NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *prev, *new_node;
	int curr_num, prev_num;

	if (*head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	curr = prev = *head;
	curr_num = prev_num = curr->n;
	if (curr == NULL || curr_num > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	} 
	while (curr != NULL)
	{
		if (curr->next == NULL || (number <= curr_num && number >= prev_num))
		{
			if (curr->next == NULL)
				prev = curr;
			new_node->next = prev->next;
			prev->next = new_node;
			return (new_node);
		}
		prev = curr;
		prev_num = curr_num;
		curr = curr->next;
		curr_num = curr->n;
	}
	return (NULL);
}
