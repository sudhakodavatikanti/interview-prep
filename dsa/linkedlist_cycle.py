"""Given the head of a singly linked list, determine if the linked list has a cycle in it. Return true if there is a cycle, false otherwise."""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def has_cycle(self, head:ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


solution = Solution()
head = [3,2,0,-4]
print(solution.has_cycle(head))