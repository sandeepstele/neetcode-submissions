from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        c1=Counter(s1)

        for i in range(0,len(s2)-len(s1)+1):

            window=s2[i:i+len(s1)]


            if Counter(window)==c1:
                return True
        return False
        