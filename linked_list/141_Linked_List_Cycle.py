'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
'''
'''
Approach
use 2 pointer, 
    slow = head
    fast = head.next
slow and fast pointer tecnique
slow pointer move 1 step at a time, 
fast pointer move 2 step at a time
    low = slow.next
    fast = fast.next.next

if there is a cycle, they will meet at some point, if there is no cycle, fast pointer will reach the end of the list


'''
from typing import List, Optional
from helper_modules.ListNode import ListNode

def hasCycle(self, head: Optional[ListNode]) -> bool:
    if head is None:
        return False
    
    if head.next is None:
        return False

    slow = head
    fast = head.next
    
    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

node1 = ListNode(3, None)
node2 = ListNode(2, None)
node3 = ListNode(0, None)
node4 = ListNode(-4, None)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

result = hasCycle(None, node1)
if result == True:
    print(True)
else:
    print(False)
    print(node1.printWholeLinkList())