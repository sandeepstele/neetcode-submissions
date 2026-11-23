class Solution:
    def isPalindrome(self, s: str) -> bool:

        t=""

        for i in s:
            if i.isalnum():
                t+=i
        t=t.lower()

        left,right=0,len(t)-1


        while left<=right:

            if t[left]==t[right]:
                left+=1
                right-=1
            
            else:
                return False
        return True
        