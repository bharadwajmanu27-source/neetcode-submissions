class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs={}

        if len(s)!=len(t):
            return False

        

        for i in s:
            if i in freqs:
                freqs[i]+=1
            else:
                freqs[i]=1

        for i in t:
            if i in freqs:
                freqs[i]-=1
            else:
                return False
        
        for i in freqs:
            if freqs[i]!=0:
                return False


        
        return True
