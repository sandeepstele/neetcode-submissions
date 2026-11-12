class Solution:
    def isValid(self, s: str) -> bool:
        mapp={")":"(","}":"{","]":"["}

        stack=[]

        for i in s:
            if i in mapp:
                if not stack:
                    return False
                if mapp[i]!=stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return not len(stack)
        