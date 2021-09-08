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
    printf(f'[Engine] Send: {command}')
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


def timematch(b, x=2):
    b = str(b)
    f.writelines('______Process started______\n')
    check()
    put('INFO max_memory ' + str(1024**3*x))
    put('INFO timeout_match ' + b)
    put('INFO timeout_turn ' + b)
    put('INFO game_type 1')
    put('INFO rule 1')
    put('INFO time_left ' + b)


def spswap():
    while True:
        try:
            text = engine.stdout.readline().strip()
            if keyboard.is_pressed('esc'):
                printf('[Stop by user]')
                break
            if 'MESSAGE' in text:
                printf('[Engine] Answer:', text.split('MESSAGE')[1].upper().strip())
            if text == 'SWAP' or ',' in text and 'MESSAGE' not in text:
                if 'DEBUG' not in text:
                    printf('[Engine]', text)
                    return text
        except:
            pass


def sp_yixin():
    lst = []
    while True:
        text = engine.stdout.readline().strip().split()
        printf(f"[Engine] Answer: {' '.join(text)}")
        try:
            if text[2].upper() == 'SWAP1':
                if text[3].upper() == 'YES':
                    printf(f'[Engine] Engine choose black')
                if text[3].upper() == 'NO':
                    printf(f'[Engine] Engine choose white')
                return 0
            elif 'MOVE4' in text or 'MOVE5' in text:
                if 'MOVE5' in text:
                    lst.append(text[3] + ',' + text[4])
                    return ' '.join(lst)
                else:
                    lst.append(text[3] + ',' + text[4])
        except:
            pass


def close():
    f.close()


def kill_engine():
    put('END')
    engine.kill()
