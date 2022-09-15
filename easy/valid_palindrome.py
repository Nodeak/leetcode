import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        mid = int(len(s) / 2)
        
        # print(mid)
        # print(s[mid:]) # Inclusive
        # print(s[:mid])  # Exclusive
        
        reg = r'[^a-z0-9]+'
        
        # lowercase
        s = s.lower()
        
        # alphanumeric onlu
        s = re.sub(reg, '', s)
        
        mid = int(len(s)/2)
        s1 = s[:mid]
        s2 = s[mid+1:]
        
        # If even
        if len(s) % 2 == 0:
            s2 = s[mid:]
            
            
        if s1 == s2[::-1]:
            return True
        return False

        
        