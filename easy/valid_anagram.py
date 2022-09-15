class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        mapS = {}
        mapT = {}
        
        for i in range(len(s)):
            
            # Fill mapS
            if s[i] not in mapS:
                mapS[s[i]] = 1
            else:
                mapS[s[i]] += 1
            
            # Fill mapT
            if t[i] not in mapT:
                mapT[t[i]] = 1
            else:
                mapT[t[i]] += 1
                
        
        print(mapS)
        print(mapT)
        if mapT != mapS:
            return False
        
        return True