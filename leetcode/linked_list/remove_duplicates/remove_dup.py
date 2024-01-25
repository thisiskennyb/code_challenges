class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)


node1.next = node2
node2.next = node3
node3.next = None

def remove_dup(head):
    curr = head
    while curr and curr.next:
        if curr.next.val == curr.val:
            curr.next = curr.next.next
            curr = curr.next
        curr = curr.next

    return head.val

print(remove_dup(node1))
