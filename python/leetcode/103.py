
from typing import *
from utils.array_to_tree import *


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        answer = []
        while q:
            size = len(q)
            arr = []
            for _ in range(0, size):
                n = q.popleft()
                arr.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)

            answer.append(arr if len(answer) % 2 == 0 else arr[::-1])

        return answer


print(Solution().zigzagLevelOrder(
    str_array_to_tree('[3,9,20,null,null,15,7]')))
