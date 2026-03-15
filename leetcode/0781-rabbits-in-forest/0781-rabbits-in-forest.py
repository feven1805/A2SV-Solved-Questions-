class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        total = 0
        myset = set(answers)
        print(myset)
        count = {}
        print(count)
        for ans in answers:
            if ans not in count or count[ans] == 0:
                total += ans + 1
                count[ans] = ans
            else:
                count[ans] -= 1
        return total

                # length of answers and then length of set