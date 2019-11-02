'''
https://open.kattis.com/contests/kgvxvo/problems/8queens
'''

board = []
def split(word): 
    return [char for char in word] 
line1 = split(input())
line2 = split(input())
line3 = split(input())
line4 = split(input())
line5 = split(input())
line6 = split(input())
line7 = split(input())
line8 = split(input())

board.append(line1)
board.append(line2)
board.append(line3)
board.append(line4)
board.append(line5)
board.append(line6)
board.append(line7)
board.append(line8)

def rows(board):
    for c in range(8):
        count = 0
        for r in range(8):
            if board[c][r] == '*':
                count += 1
            if count >= 2:
                return False
    return True

def column(board):
    for r in range(8):
        count = 0
        for c in range(8):
            if board[c][r] == '*':
                count += 1
            if count >= 2:
                return False
    return True

def diag(board):
    for c in range(8):
        for r in range(8):
            if board[c][r] == '*': 
                i, j = c,r
                while( i < 7 and j < 7): # bottom right
                    i+=1
                    j+=1
                    if board[i][j] == '*':
                        return False
                
                i, j = c,r
                while( i > 0 and j < 7): # top right
                    i-=1
                    j+=1
                    if board[i][j] == '*':
                        return False

                i, j = c,r
                while( i > 0 and j > 0): # top left
                    i-=1
                    j-=1
                    if board[i][j] == '*':
                        return False

                i, j = c,r
                while( i < 7 and j > 0): # bottom right
                    i+=1
                    j-=1
                    if board[i][j] == '*':
                        return False

    return True

x = rows(board)
y = column(board)
z = diag(board)

if (x == True and y == True and z == True):
    print('valid')
else:
    print('invalid')