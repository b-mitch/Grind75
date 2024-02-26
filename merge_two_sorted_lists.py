'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.'''

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def merge_two_lists(list1, list2):
    # Set dummy node to return the new list later
    dummy = current = ListNode()

    while list1 and list2:
        # Add whichever list value is greater
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    # If one list still has values, add them
    if list1 or list2:
        current.next = list1 if list1 else list2

    return dummy.next

# TESTS

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)

node4 = ListNode(2)
node5 = ListNode(4)
node6 = ListNode(6)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

root = merge_two_lists(node1, node4)

# Traverse merged list and convert to array
current = root
new_list = []
while current is not None:
    new_list.append(current.val)
    current = current.next

print(new_list)