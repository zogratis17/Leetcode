class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            bit = n&1 #Least Significant Bit Extraction
            res = (res << 1) | bit # Appending that bit to res
            n >>=1 # Right shift n to process next one 
        return res

        # Time : O(32)
        # Space : O(1)