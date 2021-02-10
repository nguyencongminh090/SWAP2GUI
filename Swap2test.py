import connect
import os


connect.init('alphago.exe')
inp = input('Input opening: ')
inp1 = input('Times: ')
inp = inp.split(' ')
opening = []
os.system('cls')
for i in inp:
    x = str(ord(i[:1]) - 97)
    y = str(int(i[1:]) - 1)
    opening.append(x + ',' + y)
print('Opening:', opening)

##enmove = connect.testsw(opening, int(inp1) * 1000)
##os.system('color fc')
##moves = opening
##if ',' in enmove:
##    out = enmove.split(' ')
##    for i in range(len(out)):
##        moves.append(out[i])
##board = []
##print('Engine move:', enmove)
##print(end='   ')
##for i in range(15):
##    if len(str(i)) == 2:
##        print(str(i), end='    ')
##    else:
##        print(str(i), end='     ')
##print(end='\n')
##for i in range(15):
##    line = []
##    for j in range(15):
##        if str(i) + ',' + str(j) in moves:
##            if moves.index(str(i) + ',' + str(j)) % 2 == 0:
##                line.append('X     ')
##            else:
##                line.append('O     ')
##        else:
##            line.append('.     ')
##    board.append(''.join(line))
##for i in range(len(board) - 1, -1, -1):
##    if len(str(i)) == 2:
##        print(str(i) + ' ' + board[i])
##        print(end='\n')
##        print(end='\n')
##    else:
##        print(str(i) + '  ' + board[i])
##        print(end='\n')
##        print(end='\n')
os.system('pause>nul')
