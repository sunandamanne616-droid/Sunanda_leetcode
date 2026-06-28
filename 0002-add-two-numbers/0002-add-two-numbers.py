class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy head node to simplify list assembly
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Continue loop if there are nodes left or an outstanding carry
        while l1 or l2 or carry:
            # Extract values, defaulting to 0 if a list is fully traversed
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current column
            total_sum = val1 + val2 + carry
            
            # Determine new carry and the isolated digit
            carry = total_sum // 10
            digit = total_sum % 10
            
            # Create new node for the current digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in the lists if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # Return the actual head of the resulting linked list
        return dummy_head.next