from typing import *
from utils.array_to_list import *


class Solution:
    def len(self, head: Optional[ListNode]) -> int:
        count = 0
        if not head:
            return count

        curNode = head
        while curNode:
            count += 1
            curNode = curNode.next

        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = self.len(head)

        if (N-n == 0):
            return head.next

        curNode = head
        for _ in range(N-n-1):
            curNode = curNode.next

        curNode.next = curNode.next.next
        return head


class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head


print(list_to_array(Solution2().removeNthFromEnd(
    array_to_list([1, 2, 3, 4, 5]), 2)))
print(list_to_array(Solution2().removeNthFromEnd(array_to_list([1]), 1)))
print(list_to_array(Solution2().removeNthFromEnd(array_to_list([1, 2]), 1)))
