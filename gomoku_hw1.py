import math
global board
board = [[0 for x in range(0,19)] for y in range(0,19)]

class Node:
    def __init__(self):
        self.optivalue = 0
        self.child = []

def AlphaBeta_P(node,depth,turn,alpha,beta):
    if depth == 0 or node.child == None:
        return HeuristicFun(node.nowboard)

    if turn == 2: # AI가 두는 경우
        for x in range(0,19):
            for y in range(0,19):

                if node.nowboard[x][y] == 0:
                    childnode = Node()

                    childnode.nowboard = []
                    for i in range(0,19):
                        tmp = []
                        for j in range(0,19):
                            if node.nowboard[i][j] == 0:
                                tmp.append(0)

                            elif node.nowboard[i][j] == 1:
                                tmp.append(1)

                            elif node.nowboard[i][j] == 2:
                                tmp.append(2)

                        childnode.nowboard.append(tmp)

                    childnode.nowboard[x][y] = turn
                    childnode.dx = x
                    childnode.dy = y
                    node.child.append(childnode)

        optivalue = -(math.inf)
        for i in node.child:
            i.optivalue = AlphaBeta_P(i,depth-1, 1 , alpha, beta)
            optivalue = max(optivalue, i.optivalue)

            alpha = max(alpha, optivalue)
            if beta <= alpha:
                break

        return optivalue

    elif turn == 1: # my(내) 차례인 경우
        for x in range(0,19):
            for y in range(0,19):
                if node.nowboard[x][y] == 0:
                    childnode = Node()
                    childnode.nowboard = []

                    for i in range(0,19):
                        tmp = []

                        for j in range(0,19):
                            if node.nowboard[i][j] == 0:
                                tmp.append(0)

                            elif node.nowboard[i][j] == 1:
                                tmp.append(1)

                            elif node.nowboard[i][j] == 2:
                                tmp.append(2)

                        childnode.nowboard.append(tmp)

                    childnode.nowboard[x][y] = turn
                    childnode.dx = x
                    childnode.dy = y
                    node.child.append(childnode)

        optivalue = math.inf
        
        for i in node.child:
            i.optivalue = AlphaBeta_P(i,depth-1,2,alpha,beta)

            optivalue = min(optivalue, i.optivalue)
            beta = min(beta, optivalue)

            if beta <= alpha:
                break
        return optivalue

def HeuristicFun(board):
    score = 0
    for x in range(0,16):
        for y in range(0,16):
            if x == 0:
                if board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1 and board[x+3][y] == 1:
                    if board[x+4][y] == 0:
                        score = score - 100
                    elif board[x+4][y] == 2:
                        score = score + 50
                elif board[x][y] == 1 and board[x+1][y] == 0 and board[x+2][y] == 1 and board[x+3][y] == 1:
                    if board[x+4][y] == 0:
                        score = score - 90
                    elif board[x+4][y] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 0 and board[x+3][y] == 1:
                    if board[x+4][y] == 0:
                        score = score - 90
                    elif board[x+4][y] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1:
                    score = score - 70
    
                if board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 1 and board[x][y+3] == 1:
                    if board[x][y+4] == 0:
                        score = score - 100
                    elif board[x][y+4] == 2:
                        score = score + 50
                elif board[x][y] == 1 and board[x][y+1] == 0 and board[x][y+2] == 1 and board[x][y+3] == 1:
                    if board[x][y+4] == 0:
                        score = score - 90
                    elif board[x][y+4] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 0 and board[x][y+3] == 1:
                    if board[x][y+4] == 0:
                        score = score - 90
                    elif board[x][y+4] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 1:
                    score = score - 70
                
                if board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1:
                    if board[x+4][y+4] == 0:
                        score = score - 100
                    elif board[x+4][y+4] == 2:
                        score = score + 50
                elif board[x][y] == 1 and board[x+1][y+1] == 0 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1:
                    if board[x+4][y+4] == 0:
                        score = score - 90
                    elif board[x+4][y+4] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 0 and board[x+3][y+3] == 1:
                    if board[x+4][y+4] == 0:
                        score = score - 90
                    elif board[x+4][y+4] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 1:
                    score = score - 70
                    
                if board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 2 and board[x+3][y] == 2:
                    if board[x+4][y] == 0:
                        score = score + 100
                    elif board[x+4][y] == 1:
                        score = score - 50
                elif board[x][y] == 2 and board[x+1][y] == 0 and board[x+2][y] == 2 and board[x+3][y] == 2:
                    if board[x+4][y] == 0:
                        score = score + 90
                    elif board[x+4][y] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 0 and board[x+3][y] == 2:
                    if board[x+4][y] == 0:
                        score = score + 90
                    elif board[x+4][y] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 2:
                    score = score + 70
    
                if board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 2 and board[x][y+3] == 2:
            
                    if board[x][y+4] == 0:
                        score = score + 100
                    elif board[x][y+4] == 1:
                        score = score - 50
                elif board[x][y] == 2 and board[x][y+1] == 0 and board[x][y+2] == 2 and board[x][y+3] == 2:
                    if board[x][y+4] == 0:
                        score = score + 90
                    elif board[x][y+4]==1:
                        score = score - 80
                elif board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 0 and board[x][y+3] == 2:
                    if board[x][y+4] == 0:
                        score = score + 90
                    elif board[x][y+4] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 2:
                    score = score + 70
                
                if board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 2 and board[x+3][y+3] == 2:
                    if board[x+4][y+4] == 0:
                        score = score + 100
                    elif board[x+4][y+4] == 1:
                        score = score - 50
                elif board[x][y] == 2 and board[x+1][y+1] == 0 and board[x+2][y+2] == 2 and board[x+3][y+3] == 2:
                    if board[x+4][y+4] == 0:
                        score = score + 90
                    elif board[x+4][y+4] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 0 and board[x+3][y+3] == 2:
                    if board[x+4][y+4] == 0:
                        score = score + 90
                    elif board[x+4][y+4] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 2:
                    score = score + 70
                    
            elif x == 15:
                if board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1 and board[x+3][y] == 1:
                    if board[x-1][y] == 0:
                        score = score - 100
                    elif board[x-1][y] == 2:
                        score = score + 50
                elif board[x][y] == 1 and board[x+1][y] == 0 and board[x+2][y] == 1 and board[x+3][y] == 1:
                    if board[x-1][y] == 0:
                        score = score - 90
                    elif board[x-1][y] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 0 and board[x+3][y] == 1:
                    if board[x-1][y] == 0:
                        score = score - 90
                    elif board[x-1][y] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1:
                    score = score - 70
    
                if board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 1 and board[x][y+3] == 1:
            
                    if board[x][y-1] == 0:
                        score = score - 100
                    elif board[x][y-1] == 2:
                        score = score + 50
                elif board[x][y] == 1 and board[x][y+1] == 0 and board[x][y+2] == 1 and board[x][y+3] == 1:
                    if board[x][y-1] == 0:
                        score = score - 90
                    elif board[x][y-1] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 0 and board[x][y+3] == 1:
                    if board[x][y-1] == 0:
                        score = score - 90
                    elif board[x][y-1] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 1:
                    score = score - 70
                
                if board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1:
                    if board[x-1][y-1] == 0:
                        score = score - 100
                    elif board[x-1][y-1] == 2:
                        score = score + 50
                elif board[x][y] == 1 and board[x+1][y+1] == 0 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1:
                    if board[x-1][y-1] == 0:
                        score = score - 90
                    elif board[x-1][y-1] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 0 and board[x+3][y+3] == 1:
                    if board[x-1][y-1] == 0:
                        score = score - 90
                    elif board[x-1][y-1] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 1:
                    score = score - 70

                if board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 2 and board[x+3][y] == 2:
                    if board[x-1][y] == 0:
                        score = score + 100
                    elif board[x-1][y] == 1:
                        score = score - 50
                elif board[x][y] == 2 and board[x+1][y] == 0 and board[x+2][y] == 2 and board[x+3][y] == 2:
                    if board[x-1][y] == 0:
                        score = score + 90
                    elif board[x-1][y] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 0 and board[x+3][y] == 2:
                    if board[x-1][y] == 0:
                        score = score + 90
                    elif board[x-1][y] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 2:
                    score = score + 70
    
                if board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 2 and board[x][y+3] == 2:
            
                    if board[x][y-1] == 0:
                        score = score + 100
                    elif board[x][y-1] == 1:
                        score = score - 50
                elif board[x][y] == 2 and board[x][y+1] == 0 and board[x][y+2] == 2 and board[x][y+3] == 2:
                    if board[x][y-1] == 0:
                        score = score + 90
                    elif board[x][y-1] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 0 and board[x][y+3] == 2:
                    if board[x][y-1] == 0:
                        score = score + 90
                    elif board[x][y-1] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 2:
                    score = score + 70

                if board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 2 and board[x+3][y+3] == 2:
                    if board[x-1][y-1] == 0:
                        score = score + 100
                    elif board[x-1][y-1]==1:
                        score = score - 50
                elif board[x][y] == 2 and board[x+1][y+1] == 0 and board[x+2][y+2] == 2 and board[x+3][y+3] == 2:
                    if board[x-1][y-1] == 0:
                        score = score + 90
                    elif board[x-1][y-1] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 0 and board[x+3][y+3] == 2:
                    if board[x-1][y-1] == 0:
                        score = score + 90
                    elif board[x-1][y-1] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 2:
                    score = score + 70
              
            else:
                if board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1 and board[x+3][y] == 1:
                    if board[x+4][y]== 1 or board[x-1][y]== 1:
                        score = score - 100
                    elif board[x+4][y]== 0 and board[x-1][y]== 0:
                        score = score - 100
                    elif board[x+4][y]== 2 and board[x-1][y]== 2:
                        score = score + 150 
                    elif board[x+4][y]== 2 or board[x-1][y]== 2:
                        score = score + 50
                elif board[x][y] == 1 and board[x+1][y] == 0 and board[x+2][y] == 1 and board[x+3][y] == 1:
                    
                    if board[x+4][y]== 0 and board[x-1][y]== 0:
                        score = score - 100
                    elif board[x+4][y]== 2 and board[x-1][y]== 2:
                        score = score + 100 
                    elif board[x+4][y]== 2 and board[x-1][y]== 2:
                        score = score + 100

                elif board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 0 and board[x+3][y] == 1:
                    if board[x+4][y]== 0 and board[x-1][y]== 0:
                        score = score - 100
                    elif board[x+4][y]== 2 and board[x-1][y]== 2:
                        score = score + 100 
                    elif board[x+4][y]== 2 or board[x-1][y]== 2:
                        score = score + 100

                elif board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 1:
                    if board[x+3][y] == 2 or board[x-1][y] == 2:
                        score = score + 100
                    else:
                        score = score - 100
    
                if board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 1 and board[x][y+3] == 1:
                    if board[x][y+4]==1 or board[x][y-1]==1:
                        score = score - 100
                    elif board[x][y+4]==0 and board[x][y-1]==0:
                        score = score - 100
                    elif board[x][y+4]==2 and board[x][y-1]==2:
                        score = score + 150
                    elif board[x][y+4]==2 or board[x][y-1]==2:
                        score = score + 50

                elif board[x][y] == 1 and board[x][y+1] == 0 and board[x][y+2] == 1 and board[x][y+3] == 1:
                    if board[x][y+4]==0 and board[x][y-1]==0:
                        score = score - 100
                    elif board[x][y+4]==2 and board[x][y-1]==2:
                        score = score + 100
                    elif board[x][y+4]==2 or board[x][y-1]==2:
                        score = score + 100

                elif board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 0 and board[x][y+3] == 1:
                    if board[x][y+4]==0 and board[x][y-1]==0:
                        score = score - 100
                    elif board[x][y+4]==2 and board[x][y-1]==2:
                        score = score + 100
                    elif board[x][y+4]==2 or board[x][y-1]==2:
                        score = score + 100

                elif board[x][y] == 1 and board[x][y+1] == 1 and board[x][y+2] == 1:
                    if board[x][y+3] == 2 or board[x][y-1] == 2:
                        score = score + 100
                    else:
                        score = score - 100
                
                if board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1:
                    if board[x+4][y+4]==1 or board[x-1][y-1]==1:
                        score = score - 100
                    elif board[x+4][y+4]==0 and board[x-1][y-1]==0:
                        score = score - 100
                    elif board[x+4][y+4]==2 and board[x-1][y-1]==2:
                        score = score + 150
                    elif board[x+4][y+4]==2 or board[x-1][y-1]==2:
                        score = score + 50

                elif board[x][y] == 1 and board[x+1][y+1] == 0 and board[x+2][y+2] == 1 and board[x+3][y+3] == 1:
                    if board[x+4][y+4]==0 and board[x-1][y-1]==0:
                        score = score - 100
                    elif board[x+4][y+4]==2 and board[x-1][y-1]==2:
                        score = score + 100
                    elif board[x+4][y+4]==2 or board[x-1][y-1]==2:
                        score = score + 100

                elif board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 0 and board[x+3][y+3] == 1:
                    if board[x+4][y+4]==0 and board[x-1][y-1]==0:
                        score = score - 100
                    elif board[x+4][y+4]==2 and board[x-1][y-1]==2:
                        score = score + 100
                    elif board[x+4][y+4]==2 or board[x-1][y-1]==2:
                        score = score + 100

                elif board[x][y] == 1 and board[x+1][y+1] == 1 and board[x+2][y+2] == 1:
                    if board[x+3][y+3] == 2 or board[x-1][y-1] == 2:
                        score = score + 100
                    else:
                        score = score - 100
                
                if board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 2 and board[x+3][y] == 2:
                    if board[x+4][y]==0 or board[x-1][y]==0:
                        score = score + 100
                    elif board[x+4][y]==1 or board[x-1][y]==1:
                        score = score - 100
                    elif board[x+4][y]==2 or board[x-1][y]==2:
                        score = score + 150

                elif board[x][y] == 2 and board[x+1][y] == 0 and board[x+2][y] == 2 and board[x+3][y] == 2:
                    if board[x+4][y]==0 or board[x-1][y]==0:
                        score = score + 100
                    elif board[x+4][y]==1 or board[x-1][y]==1:
                        score = score - 100

                elif board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 0 and board[x+3][y] == 2:
                    if board[x+4][y]==0 or board[x-1][y]==0:
                        score = score + 100
                    elif board[x+4][y]==1 or board[x-1][y]==1:
                        score = score - 100

                elif board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 2:
                    score = score + 100
        
                if board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 2 and board[x][y+3] == 2:
                    if board[x][y+4]==0 or board[x][y-1]==0:
                        score = score + 100
                    elif board[x][y+4]==1 or board[x][y-1]==1:
                        score = score - 100
                    elif board[x][y+4]==2 or board[x][y-1]==2:
                        score = score + 150

                elif board[x][y] == 2 and board[x][y+1] == 0 and board[x][y+2] == 2 and board[x][y+3] == 2:
                    if board[x][y+4]==0 or board[x][y-1]==0:
                        score = score + 100
                    elif board[x][y+4]==1 or board[x][y-1]==1:
                        score = score - 100

                elif board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 0 and board[x][y+3] == 2:
                    if board[x][y+4]==0 or board[x][y-1]==0:
                        score = score + 100
                    elif board[x][y+4]==1 or board[x][y-1]==1:
                        score = score - 100
                elif board[x][y] == 2 and board[x][y+1] == 2 and board[x][y+2] == 2:
                    score = score + 100
                
                if board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 2 and board[x+3][y+3] == 2:
                    if board[x+4][y+4]==0 or board[x-1][y-1]==0:
                        score = score + 100
                    elif board[x+4][y+4]==1 or board[x-1][y-1]==1:
                        score = score - 100
                    elif board[x+4][y+4]==2 or board[x-1][y-1]==2:
                        score = score + 150
                elif board[x][y] == 2 and board[x+1][y+1] == 0 and board[x+2][y+2] == 2 and board[x+3][y+3] == 2:
                    if board[x+4][y+4]==0 or board[x-1][y-1]==0:
                        score = score + 100
                    elif board[x+4][y+4]==1 or board[x-1][y-1]==1:
                        score = score - 100
                elif board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 0 and board[x+3][y+3] == 2:
                    if board[x+4][y+4]==0 or board[x-1][y-1]==0:
                        score = score + 100
                    elif board[x+4][y+4]==1 or board[x-1][y-1]==1:
                        score = score - 100
                elif board[x][y] == 2 and board[x+1][y+1] == 2 and board[x+2][y+2] == 2:
                    score = score + 100
                    
                               
    for x in range(0,15):
        for y in range(4,19):
            if x == 0:
                if board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 1 and board[x+3][y-3] == 1:
                    if board[x+4][y-4]==0:
                        score = score - 100
                    elif board[x+4][y-4]==2:
                        score = score + 50
                elif board[x][y] == 1 and board[x+1][y-1] == 0 and board[x+2][y-2] == 1 and board[x+3][y-3] == 1:
                    if board[x+4][y-4]==0:
                        score = score - 90
                    elif board[x+4][y-4]==2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 0 and board[x+3][y-3] == 1:
                    if board[x+4][y-4]==0:
                        score = score - 90
                    elif board[x+4][y-4]==2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 1:
                    score = score - 70
                    

                if board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 2 and board[x+3][y-3] == 2:
                    if board[x+4][y-4]==0:
                        score = score + 100
                    elif board[x+4][y-4] == 1:
                        score = score - 50
                elif board[x][y] == 2 and board[x+1][y-1] == 0 and board[x+2][y-2] == 2 and board[x+3][y-3] == 2:
                    if board[x+4][y-4] == 0:
                        score = score + 90
                    elif board[x+4][y-4] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 0 and board[x+3][y-3] == 2:
                    if board[x+4][y-4] == 0:
                        score = score + 90
                    elif board[x+4][y-4] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 2:
                    score = score + 70
    
            elif x == 15:
                if board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 1 and board[x+3][y-3] == 1:
                    if board[x-1][y+1] == 0:
                        score = score - 100
                    elif board[x-1][y+1] == 2:
                        score = score + 50
                elif board[x][y] == 1 and board[x+1][y-1] == 0 and board[x+2][y-2] == 1 and board[x+3][y-3] == 1:
                    if board[x-1][y+1] == 0:
                        score = score - 90
                    elif board[x-1][y+1] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 0 and board[x+3][y-3] == 1:
                    if board[x-1][y+1] == 0:
                        score = score - 90
                    elif board[x-1][y+1] == 2:
                        score = score + 80
                elif board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 1:
                    score = score - 70
                

                if board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 2 and board[x+3][y-3] == 2:
                    if board[x-1][y+1] == 0:
                        score = score + 100
                    elif board[x-1][y+1] == 1:
                        score = score - 50
                elif board[x][y] == 2 and board[x+1][y-1] == 0 and board[x+2][y-2] == 2 and board[x+3][y-3] == 2:
                    if board[x-1][y+1] == 0:
                        score = score + 90
                    elif board[x-1][y+1] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 0 and board[x+3][y-3] == 2:
                    if board[x-1][y+1] == 0:
                        score = score + 90
                    elif board[x-1][y+1] == 1:
                        score = score - 80
                elif board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 2:
                    score = score + 70
                    
            else:
                if board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 1 and board[x+3][y-3] == 1:
                    if board[x+4][y-4] == 1 or board[x-1][y+1] == 1:
                        score = score - 100
                    elif board[x+4][y-4] == 0 and board[x-1][y+1] == 0:
                        score = score - 100
                    elif board[x+4][y-4] == 2 and board[x-1][y+1] == 2:
                        score = score + 150
                    elif board[x+4][y-4] == 2 or board[x-1][y+1] == 2:
                        score = score + 50

                elif board[x][y] == 1 and board[x+1][y-1] == 0 and board[x+2][y-2] == 1 and board[x+3][y-3] == 1:
                    if board[x+4][y-4] == 0 and board[x-1][y+1] == 0:
                        score = score - 100
                    elif board[x+4][y-4] == 2 and board[x-1][y+1] == 2:
                        score = score + 100
                    elif board[x+4][y-4] == 2 or board[x-1][y+1] == 2:
                        score = score + 100

                elif board[x][y] == 1 and board[x+1][y] == 1 and board[x+2][y] == 0 and board[x+3][y] == 1:
                    if board[x+4][y-4] == 0 and board[x-1][y+1] == 0:
                        score = score - 100
                    elif board[x+4][y-4] == 2 and board[x-1][y+1] == 2:
                        score = score + 100
                    elif board[x+4][y-4] == 2 or board[x-1][y+1] == 2:
                        score = score + 100

                elif board[x][y] == 1 and board[x+1][y-1] == 1 and board[x+2][y-2] == 1:
                    if board[x+3][y-3] == 2 and board[x-1][y+1] == 2:
                        score = score + 100
                    else:
                        score = score - 100

                if board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 2 and board[x+3][y-3] == 2:
                    if board[x+4][y-4]==0 or board[x-1][y+1]==0:
                        score = score + 100
                    elif board[x+4][y-4] == 1 or board[x-1][y+1] == 1:
                        score = score - 100
                    elif board[x+4][y-4] == 2 or board[x-1][y+1] == 2:
                        score = score + 150
                elif board[x][y] == 2 and board[x+1][y-1] == 0 and board[x+2][y-2] == 2 and board[x+3][y-3] == 2:
                    if board[x+4][y-4] == 0 or board[x-1][y+1] == 0:
                        score = score + 100
                    elif board[x+4][y-4] == 1 or board[x-1][y+1] == 1:
                        score = score - 100
                elif board[x][y] == 2 and board[x+1][y] == 2 and board[x+2][y] == 0 and board[x+3][y] == 2:
                    if board[x+4][y-4] == 0 or board[x-1][y+1] == 0:
                        score = score + 100
                    elif board[x+4][y-4] == 1 or board[x-1][y+1] == 1:
                        score = score - 100
                elif board[x][y] == 2 and board[x+1][y-1] == 2 and board[x+2][y-2] == 2:
                    score = score + 100
                    

    for x in range(1,18):
        for y in range(1,18):
            if(board[x][y]!=0):
                if(board[x-1][y-1] == 2):
                    score = score + 10

                if(board[x][y-1] == 2):
                    score = score + 10

                if(board[x+1][y-1] == 2):
                    score = score + 10

                if(board[x-1][y] == 2):
                    score = score + 10

                if(board[x+1][y] == 2):
                    score = score + 10

                if(board[x-1][y+1] == 2):
                    score = score + 10

                if(board[x][y+1] == 2):
                    score = score + 10

                if(board[x+1][y+1] == 2):
                    score = score + 10
    return score

# board를 출력해주는 함수
def boardprint(board): 
    for i in range(19):
        print(board[i])

# 게임의 승패를 판단해주는 함수
def gamecount(board): 
    gamecheck = -1

    for x in range(0,19):
        for y in range(0,15):
            if(board[x][y]== 1 and board[x][y+1]== 1 and board[x][y+2]== 1 and board[x][y+3]== 1 and board[x][y+4]== 1):
                print('You win!')
                gamecheck = 3
            elif(board[x][y]== 2 and board[x][y+1]== 2 and board[x][y+2]== 2 and board[x][y+3]== 2 and board[x][y+4]== 2):
                print('AI win!')
                gamecheck = 4
                
    for x in range(4,19):
        for y in range(0,15):
            if(board[x][y]== 1 and board[x-1][y+1]== 1 and board[x-2][y+2]== 1 and board[x-3][y+3]== 1 and board[x-4][y+4]== 1):
                print('You win!')
                gamecheck = 3
            elif(board[x][y]== 2 and board[x-1][y+1]== 2 and board[x-2][y+2]== 2 and board[x-3][y+3]== 2 and board[x-4][y+4]== 2):
                print('AI win!')
                gamecheck = 4


    for x in range(0,15):
        for y in range(0,15):

            if(board[x][y]== 1 and board[x+1][y+1] == 1 and board[x+2][y+2]== 1 and board[x+3][y+3]== 1 and board[x+4][y+4] == 1):
                print('You win!')
                gamecheck = 3

            elif(board[x][y]== 2 and board[x+1][y+1]== 2 and board[x+2][y+2]== 2 and board[x+3][y+3] == 2 and board[x+4][y+4] == 2):
                print('AI win!')
                gamecheck = 4

    for x in range(0,15):
        for y in range(0,15):
            if(board[x][y]== 1 and board[x+1][y]== 1 and board[x+2][y] == 1 and board[x+3][y] == 1 and board[x+4][y] == 1):
                print('You win!')
                gamecheck = 3

            elif(board[x][y]==2 and board[x+1][y] == 2 and board[x+2][y] == 2 and board[x+3][y] == 2 and board[x+4][y] == 2):
                print('AI win!')
                gamecheck = 4

    return gamecheck

check = -1
alpha = -(math.inf)
beta = math.inf

# 프로그램이 동작하는 main 부분
while(check == -1):

    depth = 2
    print('My turn, choose my_y, my_x')
    my_x, my_y = map(int,input().split())
    if board[my_x][my_y] != 0:
        print('please choose again! my_y, my_x')
        my_x ,my_y = map(int,input().split())

    board[my_x][my_y] = 1
    boardprint(board)
    check = gamecount(board)
    if check == 3 or check == 4:
        break

    print('------------------------------------------------------------------')

    nownode = Node()
    nownode.nowboard = board
    print('AI turn')
    nownode.optivalue = AlphaBeta_P(nownode,depth,2,alpha,beta)
    dx, dy = 0, 0

    for i in nownode.child:
        if nownode.optivalue == i.optivalue:
            dx = i.dx
            dy = i.dy

    print('AI choose x, y:')
    print(dx,dy)
    board[dx][dy] = 2

    boardprint(board)
    check = gamecount(board)
    if check == 3 or check == 4:
        break

    print('------------------------------------------------------------------')