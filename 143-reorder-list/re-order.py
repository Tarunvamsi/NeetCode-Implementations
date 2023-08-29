class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Split the linked list into left and right halves
        left = head
        right = slow.next
        slow.next = None
        
        # Step 3: Push the right half onto a stack
        stack = []
        while right:
            stack.append(right)
            right = right.next
        
        # Step 4: Merge the left and right halves
        current = ListNode()  # Dummy node to build the merged list
        while left or stack:
            if left:
                current.next = left
                current = current.next
                left = left.next
            if stack:
                current.next = stack.pop()
                current = current.next
        
        return head  # Returning the reordered head node
