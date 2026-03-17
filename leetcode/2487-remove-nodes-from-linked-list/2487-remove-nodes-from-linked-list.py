# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        arr = []
        curr = head
        ans = []
        stack = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        # print(arr)
        # print(head)
        for num in arr:
            while stack and stack[-1] < num:
                stack.pop()
            stack.append(num)
        # print(stack)

        if not stack:
            return []
        first = ListNode(stack[0])
        heads = first
        i = 1
        for i in range(1, len(stack)):
            new = ListNode(stack[i])
            first.next = new
            first = new
        return heads