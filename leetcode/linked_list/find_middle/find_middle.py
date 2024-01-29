class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

def find_middle(head):
    slow = head
    fast = head

    while fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val

print(find_middle(node1))