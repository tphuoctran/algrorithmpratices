# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=-101, next=None):
        self.val = val
        self.next = next

    def printWholeLinkList(self):
        length = 0
        current = self
        listNode = []
        while current:
            listNode.append(current.val)
            length += 1
            current = current.next
        return listNode