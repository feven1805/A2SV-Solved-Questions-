class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        prefix = {0:1}
        count = 0
        summ = 0


        for num in nums:
            summ += num
            rem = ((summ % k) + k) % k
            if rem in prefix:
                count += prefix[rem]
            prefix[rem] = prefix.get(rem, 0) + 1
            
        print(prefix)
        return count
        