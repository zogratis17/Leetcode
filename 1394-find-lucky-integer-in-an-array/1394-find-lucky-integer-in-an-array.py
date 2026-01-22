from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        res = -1
        counter = Counter(arr)
        for k,v in counter.items():
            if k == v:
                res = max(k,res)
        return res