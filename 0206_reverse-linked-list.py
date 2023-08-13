import random


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"📎({self.val}, {self.next})"


def randomList():
    if not random.randint(0, 2):
        return None
    return ListNode(random.randint(0, 10), randomList())


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        print("Entering the loop.")
        print("-" * 40)
        curr = None
        while head:
            print(f"head :: {head}")
            print(f"curr :: {curr}")
            print(f"prev :: {prev}")
            curr = head
            print(f"- curr = head, so now curr = {curr}")
            head = head.next
            print(f"- head = head.next, so now head = {head}")
            curr.next = (
                prev  # Corrected line: Set current node's next to the previous node
            )
            print(f"- curr.next = prev, so now curr = {curr}")
            prev = curr
            print(f"- prev = curr, so now prev = {prev}")
            print("-" * 20)
        return prev


if __name__ == "__main__":
    sol = Solution()
    input_list = randomList()
    print("Original list: ", input_list)
    sol.reverseList(input_list)
