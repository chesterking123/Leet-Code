class Solution(object):
    def isValidSudoku(self, board):
        
        for row in board:
            row = [x for x in row if x!= '.']
            if(len(row)!=len(set(row))):
                return False
        
        col_board = [i for i in zip(*board)]
        
        for row in col_board:
            row = [x for x in row if x!= '.']
            if(len(row)!=len(set(row))):
                return False
        
        blocks=[]
        for i in range(0,9,3):
            for j in range(0,9,3):
                blocks.append(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])
        
        for row in blocks:
            row = [x for x in row if x!= '.']
            if(len(row)!=len(set(row))):
                return False

        return(True)
