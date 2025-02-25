class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev=[]
        for i in range(len(words)):
            rev.append(words[i][::-1])

        return " ".join(rev)