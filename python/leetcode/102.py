from typing import *
from utils.array_to_tree import *


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        if not root:
            return answer

        q = deque([(root, 1)])
        arr = []
        while q:
            (node, l) = q.popleft()

            if len(answer) < l-1:
                answer.append(arr)
                arr = []

            arr.append(node.val)

            if node.left:
                q.append((node.left, l+1))
            if node.right:
                q.append((node.right, l+1))

        if len(arr) > 0:
            answer.append(arr)

        return answer


class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans, level = [], [root]
        while level:
            # level에 있는 노드 꺼내서 ans에 추가
            ans.append([node.val for node in level])
            arr = []
            # level에 있는 노드의 모든 child 채우기
            for node in level:
                arr.extend([node.left, node.right])
            # arr에 leaf가 있는 경우, leaf를 모아 next level로 설정
            level = [leaf for leaf in arr if leaf]
        return ans


print(Solution2().levelOrder(str_array_to_tree('[3,9,20,null,null,15,7]')))
print(Solution2().levelOrder(str_array_to_tree('[3,9,20,2,5,15,7]')))
