class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        pref_len = len(pref)

        for s in strs:
            while pref != s[:pref_len]:
                pref_len -= 1
                if pref_len == 0:
                    return ""
                pref = pref[:pref_len]

        return pref

            # Time: O(m * S²)
            # Space: O(S)