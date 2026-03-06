# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next
        print(count)


        curr = head
        if not head.next:
            return head
        for _ in range((count//2)-1):
            curr = curr.next 
        print(head)
        print(curr)
    
        return curr.next
            
        


