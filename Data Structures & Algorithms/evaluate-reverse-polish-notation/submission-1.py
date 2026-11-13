class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack=[]

        for i in tokens:
            if i not in ["+","-","*","/"]:
                stack.append(int(i))
            else:
                b=stack.pop()
                a=stack.pop()

                if i=="+":
                    r=a+b
                elif i=="-":
                    r=a-b
                elif i=="*":
                    r= a*b
                else:
                    r = abs(a) // abs(b)

                    if (a < 0) != (b < 0):
                        r = -r
                stack.append(r)
        return stack[-1]
        