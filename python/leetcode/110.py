from typing import *
from utils.array_to_tree import *


class Solution:
    def nodeDepth(self, root: TreeNode) -> Tuple[int, bool]:
        l_d = 0
        if root.left:
            l_d, l_b = self.nodeDepth(root.left)
            if not l_b:
                return [l_d + 1, False]

        r_d = 0
        if root.right:
            r_d, r_b = self.nodeDepth(root.right)
            if not r_b:
                return [r_d + 1, False]

        return [max(l_d, r_d) + 1, abs(r_d - l_d) <= 1]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        _, balanced = self.nodeDepth(root)
        return balanced


class Solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.nodeHeight(root) >= 0

    # node의 height (balanced가 아니면 -1)
    def nodeHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        lh = self.nodeHeight(node.left)
        if lh < 0:
            return -1

        rh = self.nodeHeight(node.right)
        if rh < 0:
            return -1

        if abs(lh - rh) > 1:
            return -1
        return max(lh, rh) + 1


print(Solution2().isBalanced(str_array_to_tree("[3,9,20,null,null,15,7]")))
print(Solution2().isBalanced(str_array_to_tree("[1,2,2,3,3,null,null,4,4]")))
print(Solution2().isBalanced(str_array_to_tree("[]")))
print(Solution2().isBalanced(str_array_to_tree("[1,null,2,null,3]")))
print(Solution2().isBalanced(str_array_to_tree("[1, 2, 3, 4, null, 5]")))
print(Solution2().isBalanced(str_array_to_tree("[1, 2, 3, 4, null, 5, null, 6]")))
