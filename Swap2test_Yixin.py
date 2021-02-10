import connect
import os


inp = input('Input opening: ')
inp1 = int(input('Times: '))
inp = inp.split(' ')
opening = []
os.system('cls')
for i in inp:
    x = str(ord(i[:1]) - 97)
    y = str(14-(int(i[1:]) - 1))
    opening.append(y+','+x)
print('Opening:', opening)
connect.init('yixin.exe')
connect.yixin_balance(opening, str(inp1 * 1000))
"""enmove = connect.testsw(opening, int(inp1)*1000)
moves = opening
if ',' in enmove:
    out = enmove.split(' ')
    for i in range(len(out)):
        moves.append(out[i])
board = []
print('Engine move:', enmove)
print(end='   ')
for i in range(15):
    if len(str(i)) == 2:
        print(str(i), end='    ')
    else:
        print(str(i), end='     ')
print(end='\n')
for i in range(15):
    line = []
    for j in range(15):
        if str(j) + ',' + str(i) in moves:
            if moves.index(str(j) + ',' + str(i)) % 2 == 0:
                line.append('X     ')
            else:
                line.append('O     ')
        else:
            line.append('.     ')
    board.append(''.join(line))
for i in range(len(board)-1, -1, -1):
    if len(str(i)) == 2:
        print(str(i) + ' ' + board[i])
        print(end='\n')
        print(end='\n')
    else:
        print(str(i) + '  ' + board[i])
        print(end='\n')
        print(end='\n')"""
os.system('pause>nul')

