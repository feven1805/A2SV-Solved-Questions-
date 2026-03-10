class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        diff = [0]*(n+1)

        for l, r, d in shifts:
            if d == 1:      
                diff[l] += 1
                diff[r+1] -= 1
            else:           
                diff[l] -= 1
                diff[r+1] += 1

        for i in range(1, n):
            diff[i] += diff[i-1]

        res = []
        for i, c in enumerate(s):
            shift = diff[i] % 26
            new = (ord(c) - ord('a') + shift) % 26
            res.append(chr(new + ord('a')))

        return "".join(res)