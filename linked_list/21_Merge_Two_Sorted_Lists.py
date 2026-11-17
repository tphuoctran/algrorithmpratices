'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

'''
'''
1. compare 2 first head, which one is smaller it become the head of sorted merged list
2. travel through all note in 
'''
from helper_modules.ListNode import ListNode

def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    if list1 is None and list2 is None:
        return None
    elif list1 is None:
        return list2
    elif list2 is None:
        return list1

    #init a shadow node as result head
    head = ListNode()
    #init curr pointer 1 for list1
    curr_1 = list1
    #init curr pointer 2 for list2
    curr_2 = list2

    #compare 2 head note first
    if list1.val < list2.val:
        head = list1
        curr_1 = list1.next #move curr pointer 1 to next node
    else:
        head = list2
        curr_2 = list2.next #move curr pointer 2 to next node

    #set current pointer for head as head node
    current = head

    #either list1 or list 2 exausted first 
    while curr_1 is not None and curr_2 is not None:
        if curr_1.val < curr_2.val:
            current.next = curr_1
            curr_1 = curr_1.next
        else:
            current.next = curr_2
            curr_2 = curr_2.next

        #move current of head to next node    
        current = current.next

    #either curent remaining node in list 1 or list 2, point current next to the current node of list 1 or list 2, if its next is not none
    if curr_1 is not None:
        current.next = curr_1
    elif curr_2 is not None:
        current.next = curr_2

    return head

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
print((mergeTwoLists(None, list1, list2).printWholeLinkList()))
