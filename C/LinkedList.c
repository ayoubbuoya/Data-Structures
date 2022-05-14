#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

void push(struct Node **head_ref, int new_data)
{
    // head_ref is pointer that points to pointer

    // Aloocater New Node
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = new_data;
    // new_node next point to old pointer of head
    new_node->next = *head_ref;
    // pointer of old head begin point to the new head
    *head_ref = new_node;
}

void insertAfterNode(struct Node *node, int new_data)
{
    if (node == NULL)
    {
        printf("Given Node Can Not Be Null");
    }
    else
    {
        // allocate new node
        struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
        new_node->data = new_data;
        new_node->next = node->next;
        node->next = new_node;
    }
}

void insertAfterPos(struct Node **head_ref, int pos, int new_data)
{
    if (pos == 0)
    {
        push(head_ref, new_data);
    }
    else
    {
        // allocate new data
        struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
        new_node->data = new_data;
        struct Node *node = (struct Node *)malloc(sizeof(struct Node));
        node = (*head_ref)->next;
        int index = 1;
        while (index <= pos && node != NULL)
        {
            if (pos == index)
            {
                new_node->next = node->next;
                node->next = new_node;
                break;
            }
            else
            {
                node = node->next;
                index++;
            }
        }
    }
}

void append(struct Node **head_ref, int new_data)
{
    // Allocate new node and assign Values To it
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = NULL; // null because it is the last node in list
    if (*head_ref == NULL)
    {
        *head_ref = new_node;
    }
    else
    {
        struct Node *last = *head_ref;
        while (last->next != NULL)
        {
            last = last->next;
        }
        last->next = new_node;
    }
}

void removeKey(struct Node **head_ref, int key)
{
    struct Node *node = *head_ref;
    struct Node *prev = *head_ref;
    if (node->data == key)
    {
        *head_ref = node->next;
        free(node);
    }
    else
    {
        node = node->next;
        while (node != NULL)
        {
            if (node->data == key)
            {
                prev->next = node->next;
                free(node);
                break;
            }
            else
            {
                prev = node;
                node = node->next;
            }
        }
    }
}

// Print List From Given Node
void printList(struct Node *node)
{
    while (node != NULL)
    {
        printf("%d\n", node->data);
        node = node->next;
    }
}

int main()
{

    struct Node *head = NULL;
    struct Node *second = NULL;
    struct Node *third = NULL;
    // Allocate The 3 Nodes
    head = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));

    // tests 
    head->data = 1;
    head->next = second;
    second->data = 2;
    second->next = third;
    third->data = 3;
    third->next = NULL;
    push(&head, 10);
    append(&head, 8);
    insertAfterNode(second, 20);
    insertAfterNode(head, 30);
    insertAfterPos(&head, 0, 4);
    insertAfterPos(&head, 3, 5);
    insertAfterPos(&head, 8, 9);
    removeKey(&head, 4);
    removeKey(&head, 20);
    removeKey(&head, 9);
    printList(head);
}
