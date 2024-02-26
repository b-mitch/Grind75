'Given the head of a singly linked list, reverse the list, and return the reversed list.'

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    # If head or head.next is None, return head
    if not head or not head.next:
        return head
    # Set previous and current outside loop
    prev, current = None, head
    # Traverse the linked list
    while current:
        # Save the next before changing it
        next = current.next
        # Change next to previous
        current.next = prev
        # Set previous as current
        prev = current
        # Set current as next
        current = next
    # Return previous since current is now None
    return prev




# TESTS
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def print_list(head):
    current = head
    llist = ''
    while current:
        llist += f'{current.val} -> '
        current = current.next
    llist += 'None'
    print(llist)

print_list(node1)
print_list(reverse_list(node1))
# >> 5 -> 4 -> 3 -> 2 -> 1 -> None
