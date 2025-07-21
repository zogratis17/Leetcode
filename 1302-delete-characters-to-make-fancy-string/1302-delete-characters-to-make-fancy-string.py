class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) >= 2 and c == res[-1] and c == res[-2]:
                continue
            res.append(c)
        return "".join(res)
        
        # tc : O(N)
        # SC : O(1)