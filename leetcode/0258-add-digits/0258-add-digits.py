class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            digits = [int(d) for d in str(num)]
            num = sum(digits)
        return int(num)
