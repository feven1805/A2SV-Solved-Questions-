class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
                # track the index??
                # update the count
        ans = [0]* (len(temperatures))
        stack = []
        x = 0
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                x = stack.pop()
                ans[x] = i - x
            stack.append(i)
        return ans


        
            # print(stack[-1] , (temperatures.index(stack[-1])))
                # print(ind1, ind2)
        #         ans.append(ind2 - ind1)
        #         stack.pop()
        #     stack.append(num)
        # return ans