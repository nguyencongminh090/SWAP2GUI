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
os.system('pause>nul')
