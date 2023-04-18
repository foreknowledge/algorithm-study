from typing import *
from utils.array_to_tree import *


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        INF = 2**32
        stack = [(root, -INF, INF)]

        while stack:
            (node, min, max) = stack.pop()
            if node.left:
                if min >= node.left.val or node.left.val >= node.val:
                    return False
                stack.append((node.left, min, node.val))
            if node.right:
                if node.val >= node.right.val or node.right.val >= max:
                    return False
                stack.append((node.right, node.val, max))

        return True


class Solution2:
    beforeVal = -2**32

    def inOrder(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        if not self.inOrder(root.left):
            return False

        if self.beforeVal >= root.val:
            return False
        self.beforeVal = root.val

        if not self.inOrder(root.right):
            return False

        return True

    def isValidBST(self, root: TreeNode) -> bool:
        return self.inOrder(root)


print(Solution().isValidBST(str_array_to_tree('[2,1,3]')))
print(Solution().isValidBST(str_array_to_tree('[5,1,4,null,null,3,6]')))
print(Solution().isValidBST(str_array_to_tree('[1,1]')))
print(Solution().isValidBST(str_array_to_tree('[5,4,6,null,null,3,7]')))
print(Solution().isValidBST(str_array_to_tree('[0,null,-1]')))
