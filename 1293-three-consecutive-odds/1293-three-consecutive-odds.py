class Solution(object):
    def threeConsecutiveOdds(self, arr):
        count = 0
        for x in arr:
            if x & 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False