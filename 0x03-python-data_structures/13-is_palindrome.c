#include "lists.h"
void reverse_listint(listint_t **head);
/**
 * is_palindrome - checks if a list is palindrome
 * @head: double ptr
 *
 * Return: 1 if it is palindrome, 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head, *rev_list;

	if (*head == NULL)
		return (1);
	while (fast_ptr && fast_ptr->next)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;
	}
	rev_list = fast_ptr ? slow_ptr->next : slow_ptr;
	reverse_listint(&rev_list);
	slow_ptr = *head;
	while (rev_list && slow_ptr)
	{
		if (slow_ptr->n != rev_list->n)
			return (0);
		rev_list = rev_list->next;
		slow_ptr = slow_ptr->next;
	}
	return (1);
}

/**
 * reverse_listint - reverse a list
 * @head: pointer to first node
 *
 * Return: pointer to the first node
*/
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current)
	{
		next = current->next;
		current->next = previous;
		previous = current;
		current = next;
	}
	*head = previous;
}
