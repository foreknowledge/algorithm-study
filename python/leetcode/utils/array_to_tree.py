from typing import *
from collections import deque
from json import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def str_array_to_tree(s: str):
    return array_to_tree(loads(s))


def array_to_tree(arr):
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while i < len(arr):
        node = queue.popleft()
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_str_array(root: TreeNode):
    arr = tree_to_array(root)
    result = ''
    for val in arr:
        if val is not None:
            result += str(val)
        else:
            result += 'null'
        result += ','
    return '[' + result[:-1] + ']'


def tree_to_array(root: TreeNode) -> List[str]:
    if not root:
        return []

    queue = [root]
    result = []

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove the trailing 'null' values
    while result and result[-1] == None:
        result.pop()

    return result
