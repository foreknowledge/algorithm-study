from typing import *
from utils.array_to_tree import *


class Solution:
    prevNode = None
    firstNode = None
    secondNode = None

    def inOrder(self, root: Optional[TreeNode]):
        if not root:
            return

        self.inOrder(root.left)

        if self.prevNode and self.prevNode.val >= root.val:
            if not self.firstNode:
                self.firstNode = self.prevNode
            self.secondNode = root

        self.prevNode = root

        self.inOrder(root.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.inOrder(root)

        # swap
        tmp = self.firstNode.val
        self.firstNode.val = self.secondNode.val
        self.secondNode.val = tmp

        return tree_to_str_array(root)


print(Solution().recoverTree(str_array_to_tree('[1,3,null,null,2]')))
print(Solution().recoverTree(str_array_to_tree('[3,1,4,null,null,2]')))
