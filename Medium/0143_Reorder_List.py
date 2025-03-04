from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Deque Approach
class Solution1:
  def reorderList(self, head):
      if not head or not head.next:
          return
  
      dq = deque()
      cur = head
      while cur:
          dq.append(cur.val)  # Note: Only append the VALUE
          cur = cur.next
  
      cur = head
      for i in range(len(dq)):
          if i % 2 == 0:
              node = dq.popleft() # Connect current with node from left side of deque
          else:
              node = dq.pop()
  
          cur.val = node  # Modify the VALUE, not the node
          cur = cur.next

# Fast and Slow Pointer Approach
class Solution2:
  def reorderList(self, head):
      if not head or not head.next:
          return
  
      # 1. Find the middle of the list
      fast = slow = head
      while fast.next and fast.next.next:
          slow = slow.next
          fast = fast.next.next
  
      # 2. Reverse the second half of the list
      prev = None
      cur = slow.next
      slow.next = None  # Disconnect the first half from the second half
      while cur:
          next_node = cur.next
          cur.next = prev  # Reverse the pointer
  
          prev = cur
          cur = next_node
  
      # 3. Merge the two halves
      head1 = head
      head2 = prev  # 'prev' is now the head of the reversed second half
      while head2:  # Iterate as long as the second half has nodes
          next1, next2 = head1.next, head2.next
          head1.next = head2
          head2.next = next1
          head1, head2 = next1, next2
