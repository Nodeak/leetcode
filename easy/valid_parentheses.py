class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 0 or len(s) % 2 != 0:
            return False
        
        x = []
        
        for c in s:
            if c not in "(){}[]":
                return False
            
            if c is '(':
                x.append(')')
            elif c is '{':
                x.append('}')
            elif c is '[':
                x.append(']')
            
            if c in ")}]":
                if len(x) == 0:
                    return False
                closer = x.pop()
                if c != closer:
                    return False
        
        if len(x) > 0:
            return False
        
        return True