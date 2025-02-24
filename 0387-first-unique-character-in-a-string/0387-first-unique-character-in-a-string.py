class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)

        for index, value in enumerate(s):
            if count[value] == 1:
                return index
        return -1