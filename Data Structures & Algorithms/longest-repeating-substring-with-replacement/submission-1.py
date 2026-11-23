from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = Counter()
        mf,res,left=0,0,0

        for right in range(len(s)):

            count[s[right]]+=1

            mf= max(mf,count[s[right]])

            while (right-left+1)-mf > k:
                count[s[left]]-=1
                left+=1
            res= max(res,right-left+1)
        return res
