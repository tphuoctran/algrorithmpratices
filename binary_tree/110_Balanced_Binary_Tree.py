'''
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
'''
'''
Approach



'''
from helper_modules.TreeNode import TreeNode
from helper_modules.Helper_Binary_Tree import build_binary_tree, print_binary_tree_visually, binary_tree_to_list
def isBalanced(self, root: TreeNode | None) -> bool:
    return False

input_arr = [4,2,7,1,3,6,9]
root = build_binary_tree(input_arr)

print("\n--- Input Array ---")
print(binary_tree_to_list(root))

print("--- Input Visual Structure ---")
print_binary_tree_visually(root)

print(isBalanced(None, root))

# print("\n--- Result Array ---")
# print(binary_tree_to_list(root))

# print("--- Result Visual Structure ---")
# print_binary_tree_visually(root)
