import subprocess
import os
import time

os.system('title Swap2 Test')
f = open('Log.txt', 'a')


def put(engine, command):
    engine.stdin.write(command + '\n')
    f.write(command + '\n')


def check(engine):
    engine.stdin.write('START 15\n')
    while True:
        text = engine.stdout.readline().strip()
        if text == 'OK':
            f.write(text + '\n')
            break


def get(engine):
    """
    Return move
    :return:
    """
    while True:
        text = engine.stdout.readline().strip()
        if ',' in text:
            f.write(text + '\n')
            return text


def timematch(engine, b=None):
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
    put(engine, 'INFO max_memory 2306867200')
    put(engine, 'INFO timeout_match ' + b)
    put(engine, 'INFO timeout_turn ' + b)
    put(engine, 'INFO game_type 1')
    put(engine, 'INFO rule 1')
    put(engine, 'INFO time_left ' + b)
    return a


def begin(engine):
    """
    Start engine.
    :return:
    """
    put(engine, 'BEGIN')
    output = str(get(engine))
    return output


def playw(engine, inp):
    """
    Engine play White.
    :param engine:
    :param inp:
    :return:
    """
    put(engine, 'TURN ' + inp)
    a = getms(engine)
    if 'MESSAGE' not in a:
        return a, 0
    ev = a.split(' ')[4]
    return str(get(engine)), ev


def playb(engine, inp):
    """
    Engine play Black.
    :param engine:
    :param inp:
    :return:
    """
    put(engine, 'TURN ' + inp)
    a = getms(engine)
    if 'MESSAGE' not in a:
        return a, 0
    ev = a.split(' ')[4]
    return str(get(engine)), ev


def timeleft(engine, a):
    """
    Set timeleft for engine.
    """
    put(engine, 'INFO time_left ' + str(a))


def getms(engine):
    """
    Get engine's message!
    """
    try:
        text = engine.stdout.readline().strip()
        return text
    except:
        pass


def debug(engine):
    while True:
        try:
            text = engine.stdout.readline().strip()
            # print(text)
            if 'MESSAGE' not in text:
                return text
        except:
            pass


def close():
    f.close()


def testsw(opening, engine, times):
    engine = subprocess.Popen('Engine\\' + engine, universal_newlines=True,
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1)
    timematch(engine, times)
    put(engine, 'SWAP2BOARD')
    for i in opening:
        put(engine, i)
        time.sleep(0.5)
    put(engine, 'DONE')
    output = debug(engine)
    put(engine, 'END')
    engine.kill()
    return output
