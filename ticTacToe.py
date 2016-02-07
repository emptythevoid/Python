#conditions checked:
#
#  invalid move
#  move already made
#  winning conditions
#  stalemate conditions

theBoard = {'top-L': ' ','top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

#Returns true if any horizontal, vertical, or diagonal matches
def checkForWin(board, turn):
    if (turn == board['top-L'] and turn == board['top-M'] and turn == board['top-R']) \
       or (turn == board['mid-L'] and turn == board['mid-M'] and turn == board['mid-R']) \
       or (turn == board['low-L'] and turn == board['low-M'] and turn == board['low-R']) \
       or (turn == board['top-L'] and turn == board['mid-L'] and turn == board['low-L']) \
       or (turn == board['top-M'] and turn == board['mid-M'] and turn == board['low-M']) \
       or (turn == board['top-R'] and turn == board['mid-R'] and turn == board['low-R']) \
       or (turn == board['top-L'] and turn == board['mid-M'] and turn == board['low-R']) \
       or (turn == board['top-R'] and turn == board['mid-M'] and turn == board['low-L']):
        return True
    else:
        return

#returns False if move already exists
def checkExistingMove(board, move):
    if board[move] != ' ':
        return False
    else:
        return True
    
turn = 'X'
winflag = False

while ' ' in theBoard.values():
    printBoard(theBoard)
    
    print('Turn for ' + turn + '.  Move on which space?')
    move = input()
    if move in theBoard:
        if checkExistingMove(theBoard, move):
            theBoard[move] = turn
            if checkForWin(theBoard, turn):
                print(turn + ' wins!')
                winflag = True
                break
            else:       
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
        else:
            print('That move has already been made.  Try again.')
    else:
        print(move + ' is not a valid move.  Try again.')

printBoard(theBoard)
if not winflag:
    print('Stalemate.')
