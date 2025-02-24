class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        re = True
        for bit in bits [ -2::-1]:
            if bit:
                re= not re
            else:
                break
        return re