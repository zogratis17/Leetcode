class Solution:
    def reverseVowels(self, s: str) -> str:
        v = [c for c in s if c in "AEIOUaeiou"]
        return "".join(v.pop() if i in "AEIOUaeiou" else i for i in s)