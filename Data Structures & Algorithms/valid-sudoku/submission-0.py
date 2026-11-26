from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        rows ,columns,boxes=defaultdict(set),defaultdict(set),defaultdict(set)


        for i in range(9):
            for j in range(9):
                val =board[i][j]

                if val == ".":
                    continue
                

                box = (i//3, j//3)

                if val in rows[i] or val in columns[j] or val in boxes[box]:
                    return False
                

                rows[i].add(val)
                columns[j].add(val)
                boxes[box].add(val)
        return True
        