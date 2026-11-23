from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count=Counter()

        left,mf,result=0,0,0

        for right in range(len(s)):

            count[s[right]]+=1

            mf=max(mf,count[s[right]])

            while (right-left+1) - mf>k:
                count[s[left]]-=1
                left+=1
            result = max(result, right - left + 1)
        
        return result

        