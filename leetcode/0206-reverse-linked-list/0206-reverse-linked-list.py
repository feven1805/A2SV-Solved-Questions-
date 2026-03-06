# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        ans = []

        while curr:
            ans.append(curr.val)
            curr = curr.next

        if not ans:
            return None
        print(ans)


        res = ListNode(ans[-1])
        p = res

        for i in range(len(ans)-2, -1, -1):
            new = ListNode(ans[i])
            res.next = new
            res = res.next
        return p
            
        