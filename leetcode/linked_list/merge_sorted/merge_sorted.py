class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1_node1 = ListNode(1)
l1_node2 = ListNode(2)
l1_node3 = ListNode(4)

l1_node1.next = l1_node2
l1_node2.next = l1_node3

l2_node1 = ListNode(1)
l2_node2 = ListNode(3)
l2_node3 = ListNode(4)

l2_node1.next = l2_node2
l2_node2.next = l2_node3

def merge_sorted(list1, list2):

    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    my_head = dummy.next
    while my_head:
        print(my_head.val)
        my_head = my_head.next

    return dummy.next.val

print(merge_sorted(l1_node1, l2_node1))

