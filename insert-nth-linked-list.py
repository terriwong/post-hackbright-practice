"""Insert Node at Nth position in Linked List.

   Node is defined as:

   class Node(object):

       def __init__(self, data=None, next_node=None):
            self.data = data
            self.next = next_node

    return back the head of the linked list in the below method.
"""


def insert_node_at_nth_position(head, data, n):

    new_node = Node(data, None)

    if head is None and n == 0:
        head = new_node
        return head
    elif head is not None and n == 0:
        new_node.next = head
        head = new_node
        return head

    current = head
    curr_position = 0

    while current.next and curr_position < position - 1:

        curr_position += 1
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head
