class Solution:
    def isValid(self, s: str) -> bool:
        brak = {'}':'{', ']':'[',')':'('}
        stack = [] 

        for i in s:
            if i in brak.values():
                stack.append(i)
            elif i in brak:
                if not stack or stack.pop() != brak[i]:
                    return False
        
        return len(stack) == 0