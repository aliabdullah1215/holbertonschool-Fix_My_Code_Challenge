#include "lists.h"
#include <stdlib.h>

int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
	dlistint_t *saved_head;
	dlistint_t *tmp;
	unsigned int p;

	if (head == NULL || *head == NULL)
		return (-1);

	saved_head = *head;
	p = 0;

	while (p < index && *head != NULL)
	{
		*head = (*head)->next;
		p++;
	}

	if (*head == NULL)
	{
		*head = saved_head;
		return (-1);
	}

	tmp = *head;

	if (tmp->prev != NULL)
		tmp->prev->next = tmp->next;
	else
		saved_head = tmp->next;

	if (tmp->next != NULL)
		tmp->next->prev = tmp->prev;

	free(tmp);
	*head = saved_head;

	return (1);
}
