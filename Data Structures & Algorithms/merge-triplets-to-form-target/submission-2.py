class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        mi,mj,mk=0,0,0

        for i in range(len(triplets)):
            if target[0]<triplets[i][0] or target[1]<triplets[i][1] or target[2]<triplets[i][2]:
                continue
            else:
                if mi< triplets[i][0]:
                    mi=triplets[i][0]
                if mj<triplets[i][1]:
                    mj=triplets[i][1]
                if mk<triplets[i][2]:
                    mk=triplets[i][2]
                if [mi,mj,mk] == target:
                    return True

                

        
        return False
        