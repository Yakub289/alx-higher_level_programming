#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
* check_cycle - checks if the linked list has a cycle
* @list: linked list to check.
* Return: 1 if it has a cycle, else 0.
*/
int check_cycle(listint_t *list)
{
  listint_t *slow = list;
  listint_t *quick = list;
  if (!list)

    return (0);
  while (slow && quick && quick->next)
    {
      slow = slow->next;
      quick = quick->next->next;
      if (slow == quick)
	return (1);
    }

  return (0);
}
