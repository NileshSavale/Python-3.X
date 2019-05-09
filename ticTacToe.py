topBoard={'top-L':'','top-M':'','top-R':'','mid-L':'','mid-M':'','mid-R':'','low-L':'','low-M':'','low-R':''}

def printBoard(board):
    print (topBoard['top-L'] + '|' + topBoard['top-M'] + '|' + topBoard['top-R'])
    print('-+-+-')
    print (topBoard['mid-L'] + '|' + topBoard['mid-M'] + '|' + topBoard['mid-R'])
    print('-+-+-')
    print (topBoard['low-L'] + '|' + topBoard['low-M'] + '|' + topBoard['low-R'])

turn='X'
for i in range(9):
    printBoard(topBoard)
    print('turn on'+ turn + 'move on which space?')
    move=input("Enter the move:")
    topBoard[move]=turn
    if turn == 'X':
        turn='O'
    else:
        turn='X'

printBoard(topboard)   
        
