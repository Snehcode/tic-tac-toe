print("Welcome to TIC-TAC-TOE!Follow the reference below to choose your move and try your luck against the computer!")
print(20*' ',"   reference:    ")
print(20*' ','     |    |      ') 
print(20*' ','  0  | 1  | 2    ')
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  3  | 4  | 5    ")
print(20*' ',"-----+----+----- ")
print(20*' ',"     |    |      ")
print(20*' ',"  6  | 7  | 8    \n")


def display_board():
    print()
    print('                               reference:')
    print('     |    |     ',10*' ','     |    |   ',)
    print('  '+board[0]+'  | '+board[1]+'  | '+board[2]+'   ',10*' ','  0  | 1  | 2  ')
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |     ")
    print('  '+board[3]+'  | '+board[4]+'  | '+board[5]+'   ',10*' ',"  3  | 4  | 5  ")
    print('-----+----+-----',10*' ',"-----+----+-----")
    print('     |    |     ',10*' ',"     |    |      ")
    print('  '+board[6]+'  | '+board[7]+'  | '+board[8]+'   ',10*' ',"  6  | 7  | 8    \n\n")


def user_choice():
    while True:
        inp = input('[Player]Choose X or O: ').upper()
        if inp=='X':
            print('[PLAYER]You chose "X".\n[PLAYER]You will play first.')
            return 'X','O'
        elif inp=='O':
            print('[PLAYER] You chose "O".\n[PLAYER] COMPUTER plays first.')
            return 'O','X'
        else:
            print('[PLAYER] Enter correct input!')


def player_choice(move):
    while True:
        inp = input(f"[PLAYER] '{move}' WHERE WILL YOU MOVE?: ")
        if inp.isdigit() and int(inp)<9 and int(inp)>=0:
            inp = int(inp)
            if board[inp] == " ":
                return inp
            else:
                print(f"[PLAYER] '{move}' place is already taken.")
        else:
            print(f"[PLAYER] '{move}' Enter valid option (0 - 8).")



def winner(move,board):
    winning_place = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win_place in winning_place:
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == move:
            return True


def win_move(i,board,move):
    temp_board = list(board)
    temp_board[i] = move
    if winner(move,temp_board):
        return True
    else:
        return False


def computer_move(computer , player , board):
    for i in range(0,9):
        if board[i] == ' ' and win_move(i,board,computer):
            return i
    for i in range(0,9):
        if board[i] == ' ' and win_move(i,board,player):
            return i
    for i in [4,0,6,2,1,8,7,5,3]:
        if board[i] == ' ':
            return i

def new_game():
    while True:
        nxt = input('[PLAYER] Do you want to play again?(y/n):').lower()
        if nxt=='y':
            again = True
            break
        elif nxt=='n':
            print('See you again!')
            again = False
            break
        else:
            print('Enter correct input')
    if again:
        print('__________NEW GAME__________')
        main_game()
    else:
        return False

 
def win_check(player,computer):
    winning_place = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win_place in winning_place:      
        if board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == player:
            
            print('Congartulations!! You did it!You have won the match!')
            if not new_game():
                return False
        elif board[win_place[0]] == board[win_place[1]] == board[win_place[2]] == computer:
                print('Sorry this round the computer wins.Better luck next time!')
                if not new_game():
                    return False
    if ' ' not in board:
        print('Its a tie!!')
        if not new_game():
            return False
    return True





def main_game():
    global board
    play = True
    board =[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    player , computer = user_choice()
    display_board()
    while play:
        if player == 'X':
            X = player_choice(player)
            board[X] = player
            display_board()
            play = win_check(player , computer)
            if play:
                O = computer_move(computer , player , board)
                print(f'[COMPUTER] Entered:{O}')
                board[O] = computer
                display_board()
                play = win_check(player , computer)
        else:
            X = computer_move(computer , player , board)
            print(f'[COMPUTER] Entered:{X}')
            board[X] = computer
            display_board()
            play = win_check(player , computer)
            if play:
                O = player_choice(player)
                board[O] = player
                display_board()
                play = win_check(player , computer)

           
if __name__ == '__main__':
    main_game()
        
