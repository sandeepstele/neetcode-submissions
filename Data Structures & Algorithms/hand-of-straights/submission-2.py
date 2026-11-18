from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        c = Counter(hand)

        for i in c:
            while c[i] > 0:
                for j in range(groupSize):
                    if c[i+j]<=0:
                        return False
                    c[i+j]-=1
        return True
