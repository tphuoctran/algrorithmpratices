from collections import deque
from pathlib import Path
import sys
from typing import List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from helper_modules.TreeNode import TreeNode

def build_binary_tree(arr: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Builds a binary tree from a level-order list and returns the root node.
    """
    if not arr or arr[0] is None:
        return None

    # Create the root node and initialize the queue
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    # Process the array elements level by level
    while queue and i < len(arr):
        curr = queue.popleft()

        # Process left child
        if i < len(arr) and arr[i] is not None:
            curr.left = TreeNode(arr[i])
            queue.append(curr.left)
        i += 1

        # Process right child
        if i < len(arr) and arr[i] is not None:
            curr.right = TreeNode(arr[i])
            queue.append(curr.right)
        i += 1

    return root

def print_binary_tree_visually(node: TreeNode, level: int = 0, prefix: str = "Root: ") -> None:
    """
    Prints a visual representation of the binary tree structure.
    """
    if node is None:
        return
    
    # Print the right subtree first (appears at the top visually)
    print_binary_tree_visually(node.right, level + 1, "R---- ")
    
    # Print the current node with appropriate spacing
    print(" " * 6 * level + prefix + str(node.val))
    
    # Print the left subtree (appears at the bottom visually)
    print_binary_tree_visually(node.left, level + 1, "L---- ")

def binary_tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Converts a binary tree back into a level-order list format.
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
            
    # Clean up trailing None values to match typical array representations
    while result and result[-1] is None:
        result.pop()
        
    return result


# # 1. Define the input array
# # Example 1 from the problem description
# input_arr = [3, 9, 20, None, None, 15, 7]

# # 2. Build the tree
# root = build_binary_tree(input_arr)

# print("--- Visual Structure ---")
# print_binary_tree_visually(root)

# print("\n--- Serialized Array ---")
# print(binary_tree_to_list(root))