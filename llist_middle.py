'''Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def middle_node(head):
    slow = fast = head
    # Move fast twice and slow once for each loop
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    # When fast is the end of the list, slow is at the middle
    return slow

# TESTS

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

print(middle_node(node1).val)
# >> 4
