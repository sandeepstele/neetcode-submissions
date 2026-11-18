from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        
        c = Counter(hand)

        for i in sorted(c):
            while c[i] > 0:
                for j in range(groupSize):
                    curr= i+j
                    if c[curr]<=0:
                        return False
                    c[curr]-=1
        return True
