class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack=[]

        posp= sorted(zip(position,speed), reverse=True)


        for p,s in posp:

            t= (target-p)/s

            if not stack or t> stack[-1]:
                stack.append(t)
        return len(stack)


        