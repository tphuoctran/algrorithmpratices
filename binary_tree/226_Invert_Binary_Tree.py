'''
Given the root of a binary tree, invert the tree, and return its root.
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


'''
'''
Approach

use Queue, travel from right then left until go through of the tree, add each note to the queue, 
then dequeue and assign each dequeue left and right, until queue empty
Space issue, if tree is big, O(n) Space, time complexity O(N) time

#Use Recursion
 O(1) Space
 O(n) time
base case
If root = None -> None
if root left None and right leaf None -> bottom child node -> return root
else swap note left and right

'''
from helper_modules.TreeNode import TreeNode
from helper_modules.Helper_Binary_Tree import build_binary_tree, print_binary_tree_visually, binary_tree_to_list

def invertTree(self, root: TreeNode | None) -> TreeNode | None:
    if root is None:
        return None

    
    if root.left is None and root.right is None:
        return root
    else:
        root.left, root.right = root.right, root.left

    #Recursion
    invertTree(self, root.left)
    invertTree(self, root.right)

    return root

# 1. Define the input array
# Example 1 from the problem description
input_arr = [4,2,7,1,3,6,9]

# 2. Build the tree
root = build_binary_tree(input_arr)

print("\n--- Input Array ---")
print(binary_tree_to_list(root))

print("--- Input Visual Structure ---")
print_binary_tree_visually(root)


result_root = invertTree(None, root)
print("\n--- Result Array ---")
print(binary_tree_to_list(result_root))

print("--- Result Visual Structure ---")
print_binary_tree_visually(result_root)

