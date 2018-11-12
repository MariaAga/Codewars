def validSolution(board):
    count = [0] * 9
    for line in board:
        if len(line)!=len(set(line)):
            return False
        if 0 in line:
            return False
    board =[list(i) for i in zip(*board)]
    for line in board:
        if len(line)!=len(set(line)):
            return False
        if 0 in line:
            return False
            

    print(board)
    for i in range(9):
        a=[]
        for j in range(9):
            #a.append("{}{}".format(j%3+int(i/3)*3,int(j/3)+(i%3)*3))
            a.append(board[j%3+int(i/3)*3][int(j/3)+(i%3)*3])
        if len(a)!=len(set(a)):
            return False
        if 0 in a:
            return False
    """
    [5, 6, 1,| 8, 4, 7,| 9, 2, 3], 
    [3, 7, 9,| 5, 2, 1,| 6, 8, 4], 
    [4, 2, 8,| 9, 6, 3,| 1, 7, 5], 
    [6, 1, 3,| 7, 8, 9,| 5, 4, 2], 
    [7, 9, 4,| 6, 5, 2,| 3, 1, 8], 
    [8, 5, 2,| 1, 3, 4,| 7, 9, 6], 
    [9, 3, 5,| 4, 7, 8,| 2, 6, 1], 
    [1, 4, 6,| 2, 9, 5,| 8, 3, 7], 
    [2, 8, 7,| 3, 1, 6,| 4, 5, 9]
    """
    return True