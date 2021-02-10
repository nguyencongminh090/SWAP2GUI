import subprocess
import os
import time

os.system('title Swap2 Test')
f = open('Log.txt', 'a')


def init(engines):
    global engine
    engine = subprocess.Popen('Engine\\' + engines, universal_newlines=True,
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)


def put(command):
    engine.stdin.write(command + '\n')
    print(command)
    f.write(command + '\n')


def check(engine):
    engine.stdin.write('START 15\n')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'OK':
            f.write(text + '\n')
            break


def get():
    """
    Return move
    :return:
    """
    while True:
        text = engine.stdout.readline().strip()
        if text == 'SWAP' or ',' in text:
            f.write(text + '\n')
            return text


def timematch(b=None):
    """
    Setup time.
    :return:
    """
    if b is None:
        tm = input('Time match: ')
        a = int(tm) * 1000
        b = str(a)
    else:
        a = int(b)
        b = str(b)
    f.writelines('______Process started______\n')
    check(engine)
    put('INFO max_memory 2306867200')
    put('INFO timeout_match ' + b)
    put('INFO timeout_turn ' + b)
    put('INFO game_type 1')
    put('INFO rule 1')
    put('INFO time_left ' + b)
    return a


def begin():
    """
    Start engine.
    :return:
    """
    put('BEGIN')
    output = str(get())
    return output


def playw(inp):
    """
    Engine play White.
    :param inp:
    :return:
    """
    put('TURN ' + inp)
    a = getms()
    if 'MESSAGE' not in a:
        return a, 0
    ev = a.split(' ')[4]
    return str(get()), ev


def playb(inp):
    """
    Engine play Black.
    :param inp:
    :return:
    """
    put('TURN ' + inp)
    a = getms()
    if 'MESSAGE' not in a:
        return a, 0
    ev = a.split(' ')[4]
    return str(get()), ev


def timeleft(a):
    """
    Set timeleft for engine.
    """
    put('INFO time_left ' + str(a))


def getms():
    """
    Get engine's message!
    """
    try:
        text = engine.stdout.readline().strip()
        return text
    except:
        pass


def debug():
    while True:
        try:
            text = engine.stdout.readline().strip()
            # print(text)
            if text != '':
                print(text.upper())
            else:
                break
        except:
            break


def close():
    f.close()


def testsw(opening, times):
    timematch(times)
    put('PONDER')
    put('SWAP2BOARD')
    for i in opening:
        put(i)
        time.sleep(0.5)
    put('DONE')
    output = get()
    put('END')
    engine.kill()
    return output


def yixin_balance(opening, times):
    put('INFO timeout_turn ' + times)
    put('INFO timeout_match ' + times)
    put('INFO time_left ' + times)
    put('INFO max_node 500000000')  # Level 10
    put('INFO max_depth 225')
    put('INFO caution_factor 4')
    put('INFO thread_num 8')
    put('INFO thread_split_depth 20')
    put('INFO hash_size 21')
    put('INFO pondering 1')
    put('INFO vcthread 0')  # Maybe Global Search
    put('INFO rule 1')
    put('INFO usedatabase 1')
    put('START 15 15')
    put('yxboard')
    for i in range(len(opening)):
        if len(opening) % 2 == i % 2:
            put(opening[i] + ',1')
        else:
            put(opening[i] + ',2')
        time.sleep(0.1)
    put('done')
    put('YXBALANCETWO')
    debug()
    engine.kill()
    pass
