class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = []
        tarlen = len(part)
        tarend = part[-1]

        for curr in s:
            res.append(curr)

            if curr == tarend and len(res) >= tarlen:
                if "".join(res[-tarlen:]) == part:
                    del res[-tarlen:]
        
        return "".join(res)


        # Time : O(n*m)
        # Space : O(n)