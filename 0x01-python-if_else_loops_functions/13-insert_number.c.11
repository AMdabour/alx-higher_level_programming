#include "lists.h"

/**
 * insert_node - insert a node in a sorted linked list
 * @head: the linked list to check
 * @number: the integer to be added
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *current, *previuos;

	current = *head;
	previuos = *head;
	new_node = (listint_t *) malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
		*head = new_node;

	else
	{
		while (current != NULL)
		{
			if (new_node->n <= current->n)
			{
				new_node->next = current;
				previuos->next = new_node;
				return (new_node);
			}
			previuos = current;
			current = current->next;
		}
		previuos->next = new_node;
		return (new_node);
	}

	return (new_node);
}
