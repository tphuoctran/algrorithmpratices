'''
Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]
Example 2:

Input: head = [5], n = 1

Output: []
Example 3:

Input: head = [1,2], n = 2

Output: [2]
Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''
'''
Approach
Due to requirement is remove nth from the botto, have to travel to the end of list to find last node

1. Travel from head to end of list
    add to each node to an list nodes

Notice:
when remove a node
1 -> 2 
    1.next -> 2.next 
if n = len(nodes) -> remove head, just set head = head.next, then return new head

1 -> 2 -> 3 -> 4
if n = 1, then
    3 -> None
if n = 2 then
    2 -> 4

2. set curr = len(nodes) - n, the current index of removed node in the list nodes

3. if curr > 0, then set the node before curr nodes[ curr - 1].next to nodes[curr].next

    if curr <=0,  set head = head.next
    
4. return head
'''
from helper_modules.ListNode import ListNode

def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
    if head.next is None and n == 1:
        return None

    nodes = list()
    current = head

    while current is not None:
        nodes.append(current)
        current = current.next 

    curr = len(nodes) - n

    if curr > 0:
        nodes[curr - 1].next = nodes[curr].next
    else:
        head = head.next
        
    return head




list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(removeNthFromEnd(None, list1, 3).printWholeLinkList())

list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))
print(removeNthFromEnd(None, list1, 4).printWholeLinkList())