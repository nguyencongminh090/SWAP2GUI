import time
import subprocess
import keyboard


f = open('Log.txt', 'w')


# noinspection PyGlobalUndefined
def init(engines, scrts):
    global engine, scrt
    engine = subprocess.Popen('Engine\\' + engines + '.exe', universal_newlines=True,
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, bufsize=1, creationflags=0x00000008)
    scrt = scrts
    

def printf(*txt):
    try:
        txt = [str(i) for i in txt]
        scrt.insert('insert', ' '.join(txt) + '\n')
    except:
        pass


def put(command):
    try:
        engine.stdin.write(command + '\n')
        f.write(command + '\n')
    except:
        print('Engine is not exist')


def check():
    engine.stdin.write('START 15\n')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'OK':
            f.write(text + '\n')
            break


def timematch(b=None, x):
    b = str(b)
    f.writelines('______Process started______\n')
    check()
    put('INFO max_memory ' + str(1024**3*x))
    put('INFO timeout_match ' + b)
    put('INFO timeout_turn ' + b)
    put('INFO game_type 1')
    put('INFO rule 1')
    put('INFO time_left ' + b)


def getms():
    """
    Get engine's message!
    """
    try:
        text = engine.stdout.readline().strip()
        return text
    except:
        pass


def spswap():
    while True:
        try:
            text = engine.stdout.readline().strip()
            if keyboard.is_pressed('esc'):
                printf('Stop by user!')
                break
            if 'MESSAGE' in text:
                printf(text.split('MESSAGE')[1].upper())
            if text == 'SWAP' or ',' in text and 'MESSAGE' not in text:
                if 'DEBUG' not in text:
                    printf(text)
                    return text
        except:
            pass


def close():
    f.close()


def kill_engine():
    put('END')
    engine.kill()


# New Function
def evaluation(num):
    """
    - Max evaluation: 10000
    - Testcase:
    + [19] = 0.19
    + [-30] = -0.3
    + [-227] = -2.27
    + [-225] = -2.25
    + [-M22] = Lose in 22 moves
    + [6500] = +65
    -> Convert to win-rate:
    + [0.19] = (0.19 + 200) / 100 = 50.095%
    """
    try:
        num = float(num)
        if num > 1000:
            k = open('Error.txt', 'a+')
            k.write('*** ' + time.ctime() + ' ***\n')
            msg = 'Raise Error:' + str(num) + ' > ' + '10000'
            k.write(msg + '\n')
            k.write('~' * len(msg) + '\n')
            k.close()
            return 'Error: {} > {}'.format(num, 1000)
        num = ((num / 10 + 100) / 200) * 100
        return '{}%'.format(round(num, 2))
    except:
        if str(num).isascii():
            if '-' in num:
                solve = 'Lose in ' + num.split('-M')[1] + (' moves' if num.split('-M')[1] >= '2' else ' move')
                return solve
            elif 'M' in num:
                solve = 'Win in ' + num.split('M')[1] + (' moves' if num.split('M')[1] >= '2' else ' move')
                return solve
            else:
                k = open('Error.txt', 'a+')
                k.write('*** ' + time.ctime() + ' ***\n')
                msg = 'Raise Error: ' + str(num) + '(Win/Lose)'
                k.write(msg + '\n')
                k.write('~' * len(msg) + '\n')
                k.close()
                raise ValueError(msg + ' (Win/Lose)')
        else:
            k = open('Error.txt', 'a+')
            k.write('*** ' + time.ctime() + ' ***\n')
            msg = 'Raise Error: {} (String)'.format(num)
            k.write(msg + '\n')
            k.write('~' * len(msg) + '\n')
            k.close()
            raise ValueError(msg)
