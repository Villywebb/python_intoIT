from random import randint
SHOTS = 5
BOARD_SIZE = 5
HITCHANCE = 65 #chance of hitting target in percent

class Player:
    #TODO: Implement own hitchance variable
    def __init__(self,name):
        self.name = name
        self.board = BOARD_SIZE * [1]
        self.hits = 0
        
    def shoot(self,target):
        if randint(1,100) <= HITCHANCE:
            if(self.board[target-1] != 0):
                self.board[target-1] = 0
                self.hits+=1
                return "hit_open"
            else:
                return "hit_closed"
        else:
            return "miss"
       
def printStart():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("             Biathlon\n")
    print("         a hit or miss game")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\nYou got",SHOTS,"shots\n")

def printBoard(board):
    text = " ".join(str(i) for i in range(1,len(board)+1))
    print(f"\n{text}")
    for b in board:
        if b == 1:print("*","",end="")
        else:print(b,"",end="")
    print()

def start(board):
    printStart()
    printBoard(board)

def askTarget(i):
    while True:
        try:
            print("\nShot nr",i,"at: ",end="")
            target = int(input())
            if target <=BOARD_SIZE and target > 0:
                break
            else:
                print("\nWRITE BETWEEN 1 -",BOARD_SIZE)
        except(ValueError):
            print("\nWRITE AN INTEGER")
    return target

def game(p):
    start(p.board)
    for i in range(1, SHOTS + 1):
        
        target = askTarget(i)
        shotStatus = p.shoot(target)
        if shotStatus == "hit_open": print("\nHit on an open target")
        elif shotStatus == "hit_closed": print("\nHit on closed target")
        elif shotStatus == "miss": print("\nMiss")
        else: raise ValueError("Issue with shotStatus")

        printBoard(p.board)

    print("\nYou hit",p.hits,"of",SHOTS)

def askPlayerAmount():
    while True:
        try:
            print("How many players? ",end="")
            amount = int(input())
            if amount > 0:return amount
            else: print("AT LEAST 1 PLAYER")
        except(ValueError):
            print("INTEGERS ONLY")

def askPlayAgain():
    print("\nPlay again? (y/n) ",end="")
    if input().lower() == "y":return True
    else: return False

def printResults(players):
    print()
    for p in players:
        print(p.name," --- ",p.board," --- ", p.hits)

def printWinner(players):
    highScore = max(p.hits for p in players)
    highPlayers = [p for p in players if p.hits == highScore]
  
    if len(highPlayers) == 1:
        print(f"THE WINNER IS: {highPlayers[0].name}!!!")
    else:
        names = ", ".join(p.name for p in highPlayers)
        print(f"ITS A TIE BETWEEEN: {names}")

def askPlayer():
    print("What's your name? ",end="")
    return input()

def gameRunner():
    while True:
        players = []
        for _ in range(askPlayerAmount()):
            p = Player(askPlayer())
            game(p)
            players.append(p)
        printResults(players)
        printWinner(players)
        if(not askPlayAgain()):
            break

gameRunner()