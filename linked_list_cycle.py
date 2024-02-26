'''Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def has_cycle(head):
    if head is None:
        return False
    # Set slow and fast pointers
    slow, fast = head, head.next
    # Traverse linked list with fast and slow pointer
    while fast is not None and fast.next is not None:
        # If a cycle exists, slow and fast will eventually be equal
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    # If not, the loop will exit because fast pointer reached the end
    return False


# TESTS
        
numbs = [3,2,0,-4]

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(has_cycle(node1))
