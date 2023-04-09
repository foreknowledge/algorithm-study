from typing import *
from utils.array_to_tree import *


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def func(p, q):
            if not p or not q:
                return p == q

            return (p.val == q.val) and func(p.left, q.right) and func(p.right, q.left)

        return func(root.left, root.right)
