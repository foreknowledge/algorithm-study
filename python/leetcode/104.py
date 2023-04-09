from typing import *
from utils.array_to_tree import *


class Solution:
    def deeper(self, tree: Optional[TreeNode], depth: int) -> int:
        if not tree:
            return depth - 1
        return max(
            self.deeper(tree.left, depth + 1), self.deeper(tree.right, depth + 1)
        )

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.deeper(root, 1)


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        maxDepth = 0
        queue = [(root, 1)]

        while queue:
            (tree, depth) = queue.pop(0)
            maxDepth = depth

            if tree.left:
                queue.append((tree.left, depth + 1))
            if tree.right:
                queue.append((tree.right, depth + 1))

        return maxDepth


print(Solution2().maxDepth(str_array_to_tree("[3,9,20,null,null,15,7]")))
print(Solution2().maxDepth(str_array_to_tree("[1,null,2]")))
