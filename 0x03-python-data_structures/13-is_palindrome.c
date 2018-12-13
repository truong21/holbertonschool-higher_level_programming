#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head of singly linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *middle, *rev_head;

	middle = mid_list(head);
	rev_head = rev_list(&middle);
	while (rev_head != NULL)
	{
		if (rev_head->n != (*head)->n)
			return (0);
		rev_head = rev_head->next;
		*head = (*head)->next;
	}
	return (1);

}
/**
 * mid_list - locate the middle node of the linked list
 * @head: pointer to head of linked list
 * Return: pointer to middle of linked list
 */
listint_t *mid_list(listint_t **head)
{
	listint_t *slow, *fast;

	slow = fast = *head;
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow);
}
/**
 * rev_list - reverse the second half of the linked list
 * @middle: pointer to middle node
 * Return: pointer to first node of reverse list
 */
listint_t *rev_list(listint_t **middle)
{
	listint_t *temp, *prev, *curr;

	temp = prev = NULL;
	curr = *middle;
	while (curr != NULL)
	{
		temp = curr->next;
		curr->next = prev;
		prev = curr;
		curr = temp;
	}
	return (prev);
}
