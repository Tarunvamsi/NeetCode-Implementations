'''You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 '''

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to serve as the starting point of the merged list.
        dummy = ListNode()
        tail = dummy  # Initialize tail to point to the dummy node.

        # Loop until either list1 or list2 becomes None.
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2.
            if list1.val < list2.val:
                # Attach the current node from list1 to the merged list.
                tail.next = list1
                list1 = list1.next  # Move list1 pointer forward.
            else:
                # Attach the current node from list2 to the merged list.
                tail.next = list2
                list2 = list2.next  # Move list2 pointer forward.
            
            tail = tail.next  # Move the tail of the merged list to the last attached node.

        # Attach any remaining nodes from either list1 or list2.
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # Return the merged list starting from the node after the dummy node.
        return dummy.next
