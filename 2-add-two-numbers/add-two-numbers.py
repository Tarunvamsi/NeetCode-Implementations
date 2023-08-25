# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head

        # Initialize a carry for addition
        carry = 0
        
        # Iterate through both linked lists and the carry
        while l1 or l2 or carry:
            # Get the values of the current nodes (default to 0 if nodes are None)
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            # Calculate the sum of values and the carry for the next digit
            total_sum = value1 + value2 + carry
            carry = total_sum // 10  # Calculate the carry
            current_digit = total_sum % 10  # Calculate the value for the current digit

            # Create a new node for the current digit and append it to the result
            current.next = ListNode(current_digit)

            # Update pointers
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result, excluding the dummy head
        return dummy_head.next
            
        
