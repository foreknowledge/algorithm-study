from typing import *
from utils.array_to_tree import *


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        result = []

        result += self.inorderTraversal(root.left)
        result += [root.val]
        result += self.inorderTraversal(root.right)

        return result


# Solution2. 문법 축약 버전
class Solution2:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            + self.inorderTraversal(root.right)
            if root
            else []
        )


print(Solution().inorderTraversal(array_to_tree([1, None, 2, 3])))
print(Solution().inorderTraversal(array_to_tree([])))
print(Solution().inorderTraversal(array_to_tree([1])))
print(Solution().inorderTraversal(array_to_tree([1, 2, None, 3, 4, None, 5])))
