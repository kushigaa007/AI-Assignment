board = [
  ['', '', ''],
  ['', '', ''],
  ['', '', '']
];
w=3
h=3
ai = 'X'
human = 'O'
CurrentPlayer = human
print("HUMAN PLAYS 0")
print("AI PLAYS X")
print("Your Turn, human !")

def checker(a,b,c):
    return (a==b and b==c and a!='')
def checkWinner():
    winner = "CONTINUE";
    #Horizontal
    for i in range(3):
        if(checker(board[i][0],board[i][1],board[1][2])):
            winner = board[i][0];
    #Vertical
    for i in range(3):
        if(checker(board[0][i], board[1][i], board[2][i])):
            winner = board[0][i];
    #Diagonal
        if(checker(board[0][0], board[1][1], board[2][2])):
            winner = board[0][0];
        if(checker(board[2][0],board[1][1],board[0][2])):
            winner = board[2][0]
        openSpots = 0;
        for i in range(3):
            for j in range(3):
                if(board[i][j]==''):
                    openSpots=openSpots+1
        if(winner == "CONTINUE" and openSpots == 0):
            return "tie"
        else:
            return winner
def inputs():
    if(CurrentPlayer == human):
        r = int(input("Enter Row"))-1
        c = int(input("Enter Col"))-1
    if(board[r][c]==''):
        board[r][c]=human
        currentPlayer = ai
        bestMove()
        prints()

def prints():
    for i in range(3):
        for j in range(3):
            if(board[i][j]==''):
                print("*",end="")
            print(board[i][j]+"\t",end="")
        print("\n")
    
def results():
    result = checkWinner()
    if(result!="CONTINUE"):
        if(result=="tie"):
            print("TIE")
        else:
            print(result + "WINS")

def bestMove():
    bestScore = -999;
    move = {"row":0 , "column":0}
    for i in range(3):
        for j in range(3):
            if(board[i][j]==''):
                board[i][j] = ai
                score = minimax(board,0,False)
                board[i][j]=''
                if(score>bestScore):
                    bestScore = score;
                    move["row"]=i
                    move["column"]=j
    board[move["row"]][move["column"]]=ai
    currentPlayer = human
scores = {"X":10 , "O":-10, "tie":0}

def minimax(board,depth, isMaximizing):
    result = checkWinner()
    if(result !="CONTINUE"):
        return scores[result]
    if(isMaximizing):
        bestScore = -999
        for i in range(3):
            for j in range(3):
                if(board[i][j]==''):
                    board[i][j]=ai
                    score = minimax(board,0,False)
                    board[i][j]=''
                    bestScore = max(score,bestScore)
    else:
        bestScore = 999
        for i in range(3):
            for j in range(3):
                if(board[i][j]==''):
                    board[i][j] = human
                    score = minimax(board,depth+1,True)
                    board[i][j]=''
                    bestScore=min(score,bestScore)
    return bestScore

while(checkWinner() == "CONTINUE"):
    inputs()
results()
