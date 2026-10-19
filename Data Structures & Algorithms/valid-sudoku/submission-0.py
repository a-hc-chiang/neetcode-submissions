class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # checking each row 
        for row in board:
            cnt = Counter(row)
            for key, val in cnt.items():
                if key != "." and val > 1:
                    return False
        # checking each col 
        for i in range(9):
            counts = [0] * 9
            for row in board:
                if row[i] != ".":
                    counts[int(row[i]) - 1] += 1
            for c in counts:
                if c > 1: 
                    return False
        # checking each quadrant
        for i in range(3):
            # print("hello!")
            start, end = i*3, (i+1)*3
            for j in range(3):
                counts = [0] * 9
                start2, end2 = j*3, (j+1)*3
                print(start, end, start2, end2)
                for k in range(start, end): 
                    for l in range(start2, end2):
                        if board[k][l] != ".":
                            counts[int(board[k][l])-1] += 1
            # print(counts)
                for count in counts:
                    if count > 1:
                        return False
        return True
