class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        friends = []
        for i in range(n):
            friends.append(i)
        start = 0
        while len(friends) > 1:
            remove = (start + k - 1) % len(friends)
            friends.pop(remove)
            start = remove
        return friends[0] + 1