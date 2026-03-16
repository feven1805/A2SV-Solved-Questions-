from collections import Counter
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count5 = 0
        count10 = 0
        for bill in bills:
            if bill == 5:
                count5 += 1
                
            elif bill == 10:
                if count5 == 0:
                    return False
                count5 -= 1
                count10 += 1

            else:
                if count10 > 0 and count5 > 0:
                    count10 -= 1
                    count5 -= 1
                elif count5 >= 3:
                    count5 -= 3
                else:
                    return False

        return True



            
        # count = Counter(bills)
        # print(count)
        # ans = False
        # for ch in bills:
        #     if ch == 5:
        #         count[ch] += 1
        #     if ch == 10:
        #         if count[5] >= 2:
        #             ans = True
        #         else:
        #             ans = False
        #     if ch == 20:
        #         if count[5] >= 4 or count[10] >= 2:
        #             ans = True
        #         else:
        #             ans = False
        #     if ans:
        #         return True
        #     else:
        #         return False



            # if ch == 5:
            #     continue
            # else:
            #     needed = ch - 5
            #     if needed in count:
            #         count[needed] -= 1
            #         return True
            # return False


        


