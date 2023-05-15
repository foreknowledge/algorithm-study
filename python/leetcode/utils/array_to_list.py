class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def array_to_list(arr):
    if not arr:
        return None

    # 첫 번째 노드 생성
    head = ListNode(arr[0])
    curr = head

    # 나머지 노드 생성
    for i in range(1, len(arr)):
        curr.next = ListNode(arr[i])
        curr = curr.next

    return head


def list_to_array(head):
    arr = []
    curr = head

    # 노드를 돌면서 배열에 추가
    while curr:
        arr.append(curr.val)
        curr = curr.next

    return arr
