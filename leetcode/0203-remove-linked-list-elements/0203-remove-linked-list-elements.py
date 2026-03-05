# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        # dummy.val = 0
        # dummy.next = head
        
        ans = []
        dummy = ListNode(-1,head)
        prev = dummy
        while prev  and prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next

            else:
                prev = prev.next

        return dummy.next
            
        # # print(ans)        
        # res = ListNode(ans[0])
        # temp = ListNode(ans[0])
        # for i in range(1,len(ans)):
        #     new = ListNode(ans[i])
        #     temp.next = new
        #     temp = temp.next 





        