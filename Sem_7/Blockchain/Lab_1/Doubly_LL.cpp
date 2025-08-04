#include <bits/stdc++.h>
using namespace std;

class List
{
public:
    int data;
    List *prev;
    List *next;

    List(int data)
    {
        this->data = data;
        this->prev = nullptr;
        this->next = nullptr;
    }
};

// Append node at the end of the list
void appendNode(List *&head, int data)
{
    List *newNode = new List(data);

    if (head == nullptr)    
    {
        head = newNode;
        return;
    }

    List *temp = head;
    while (temp->next != nullptr)
    {
        temp = temp->next;
    }

    temp->next = newNode;
    newNode->prev = temp;
}

// Print the list
void printLL(List *head)
{
    List *temp = head;
    while (temp != nullptr)
    {
        cout << "Block address: " << temp << endl;
        cout << "Block data: " << temp->data << endl;
        temp = temp->next;
    }
}

// Print it in reverse
void printReverse(List *head)
{
    if (!head)
        return;

    List *temp = head;
    while (temp->next != nullptr)
    {
        temp = temp->next;
    }

    while (temp != nullptr)
    {
        cout << "Block address: " << temp << endl;
        cout << "Block data: " << temp->data << endl;
        temp = temp->prev;
    }
}

int main()
{
    List *head = nullptr;

    appendNode(head, 10);
    appendNode(head, 20);
    appendNode(head, 30);

    printLL(head);

    return 0;
}
