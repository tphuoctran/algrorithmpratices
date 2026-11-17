'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:

Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 
Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
'''
Approach
iteratation
The algorithm for reversing a linked list is an iterative algorithm which involves 3 pointers, prev, current, and next_.
current points to the node we are currently reversing.
prev is the last node that was reversed, and also the node that current.next will point to after reversing.
next_ is the next node we will reverse. We need a pointer to this node before we overwrite the current.next so we can continue reversing the list in the next iteration.
When the iteration completes, current will be None, and prev will be the new head of the linked list.

recursion

1 -> 2
    2 -> 3
        3 -> 4
            4 -> 5
                5 -> None

Notice that when do reverse 2 node, we do point the current node to prev node
and we repeat until the current Node is null end of list
general case: list with only 2 nodes
1 -> 2
set 2 -> 1, and 2 become new head

#Base Case
    current -> None -> return node as head
    5 -> None -> return 5

# Recursive step (General case)
recur(prev, current)
current -> prev, and return head = current
    recur(None, 1) 1 ->
        recur(1, 2) 2 -> 1
            recur(2, 3) 3 -> 2
                recur(3, 4) 4 -> 3
                    recur(4, 5) 5 -> 4

'''

from helper_modules.ListNode import ListNode
def reverseList_iteratation(self, head: ListNode) -> ListNode:
    
    if head is None:
        return None
    
    if head.next is None:
        return head

    if head.next.next is None:
        head.next.val, head.val = head.val, head.next.val
        return head

    prev = None
    current = head

    while current:
        current_next = current.next
        current.next = prev
        prev = current
        current = current_next

    return prev

def reverseList_recur(self, head: ListNode) -> ListNode:

    # Base Case for empty list
    if head is None:
        return None

    # Start the recursion with prev as None and current as head
    prev = None
    current = head
    return reverseList_recursion(prev, current)
    


def reverseList_recursion(prev: ListNode , current: ListNode) -> ListNode:
    # Base Case: reached the end of the original list
    if current.next is None:
        current.next = prev
        return current  # This is the new head of the reversed list

    # Recursive step: capture the new head returned from deeper levels
    new_head = reverseList_recursion(current, current.next)

    # Reverse the link for the current node
    current.next = prev

    # Pass the new head all the way back up the call stack
    return new_head
    


list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(list1.printWholeLinkList())
print(reverseList_iteratation(None, list1).printWholeLinkList())

# list2 = ListNode(1, ListNode(2, None))
# print(list2.printWholeLinkList())
# print(reverseList_iteratation(None, list2).printWholeLinkList())

list3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
print(list3.printWholeLinkList())
head = reverseList_recur(None, list3)
print(head.val)
# print(reverseList_recur(None, list3).printWholeLinkList())