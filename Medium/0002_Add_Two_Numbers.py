# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Optimal Approach
class Solution:
    def addTwoNumbers(self, l1, l2):
        # Initialize a dummy head node (simplifies list construction)
        dummy_head = ListNode(0)
        # Pointer to the current node in the result list
        current = dummy_head
        # Initialize carry to 0
        carry = 0

        # Loop until both lists are exhausted and there's no carry left
        while l1 or l2 or carry != 0:
            combined_value = 0  # Sum of digits + carry

            # Add digit from l1 if it exists
            if l1:
                combined_value += l1.val
                l1 = l1.next  # Move to next node in l1

            # Add digit from l2 if it exists
            if l2:
                combined_value += l2.val
                l2 = l2.next  # Move to next node in l2

            # Calculate the result digit and carry
            result_digit = (combined_value + carry) % 10
            carry = (combined_value + carry) // 10

            # Create a new node and add it to the result list
            current.next = ListNode(result_digit)
            current = current.next  # Move the pointer

        # Return the actual head of the result list (skip the dummy head)
        return dummy_head.next
