class Solution:
    def isValid(self, s: str) -> bool:
        brac = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for c in s:
            if c in brac.values():
                stack.append(c)
            elif c in brac:
                if not stack or stack[-1] != brac[c]:
                    return False
                stack.pop()
                
        return not stack
                 


                