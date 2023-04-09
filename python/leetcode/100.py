from typing import *
from utils.array_to_tree import *


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None or q == None:
            return p == q

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


print(Solution().isSameTree(str_array_to_tree("[1,2,3]"), str_array_to_tree("[1,2,3]")))
print(
    Solution().isSameTree(str_array_to_tree("[1,2]"), str_array_to_tree("[1,null,2]"))
)
print(Solution().isSameTree(str_array_to_tree("[1,2,1]"), str_array_to_tree("[1,1,2]")))
print(Solution().isSameTree(str_array_to_tree("[]"), str_array_to_tree("[]")))
