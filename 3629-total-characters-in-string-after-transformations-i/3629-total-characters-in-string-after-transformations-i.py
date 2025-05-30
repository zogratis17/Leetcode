class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD, str_len = 10**9 + 7, 0
        freq, dp_prev = [0] * 26, [1] * 26
        for ch in s: 
            freq[ord(ch) - ord('a')] += 1

        for tt in range(t):
            dp_curr = [0] * 26
            for i in range(25): # 'a'..'y' shift to next letter
                dp_curr[i] = dp_prev[i + 1]
            dp_curr[25] = (dp_prev[0] + dp_prev[1]) % MOD # expand z-->ab
            dp_prev = dp_curr

        for i in range(26):
            str_len = (str_len + freq[i] * dp_prev[i]) % MOD

        return str_len