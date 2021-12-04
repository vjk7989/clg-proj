board = ['-','-','-','-','-','-','-','-','-']

def Board():
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])

    print('-----------')

    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])

    print('-----------')

    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])


def check_win():
    plr1 = 'x'
    plr2 = 'o'
    if board[0]==board[1]==board[2] == plr1 or board[0]==board[1]==board[2] == plr2 :
        return  True
    elif board[3]==board[4]==board[5] == plr1 or board[3]==board[4]==board[5] == plr2 :
        return  True
    elif board[6]==board[7]==board[8] == plr1 or board[6]==board[7]==board[8] == plr2 :
        return  True
    elif board[3]==board[0]==board[6] == plr1 or board[3]==board[0]==board[6] == plr2 :
        return  True
    elif board[1]==board[4]==board[7] == plr1 or board[1]==board[4]==board[7] == plr2 :
        return  True
    elif board[2]==board[5]==board[8] == plr1 or board[2]==board[5]==board[8] == plr2 :
        return  True
    elif board[0]==board[4]==board[8] == plr1 or board[0]==board[4]==board[8] == plr2 :
        return  True
    elif board[6]==board[5]==board[2] == plr1 or board[6]==board[5]==board[2] == plr2 :
        return  True
    else:
        return False
def Input(Board):
    pos = int(input("Enter the position : "))
    if Board[pos-1] != '-' :
        print("The position is already been chosen pick other")
        return Input(Board)
    else:
        return pos

plr1 = input("Enter your name :")
plr2 = input("Enter your name :")


