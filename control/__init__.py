from control.connect import *
import time


class Control:
    def __init__(self, opening: str, time_in, engine, protocol: str, scrt, memory=2):
        self.opening = opening
        self.time = time_in
        self.engine = engine
        self.protocol = protocol
        self.scrt = scrt
        self.memory = int(memory)

    def printf(self, *txt, endl='\n'):
        try:
            txt = [str(i) for i in txt]
            self.scrt.insert('insert', ' '.join(txt) + endl)
        except:
            pass

    @staticmethod
    def pktool(move, q):
        if q == 0:
            x = move[0]
            y = move[1:]
            return str(ord(x) - 97) + ',' + str(15 - int(y))
        if q == 1:
            x = int(move.split(',')[0])
            y = int(move.split(',')[1])
            return str(chr(x + 97)) + str(int(15 - y))

    def gomocup(self, opening, time_in, engine):
        init(engine, self.scrt)
        timematch(time_in, self.memory)
        put('SWAP2BOARD')
        for i in opening:
            put(i)
            time.sleep(0.4)
        put('DONE')
        move = spswap().split()
        kill_engine()
        if move != 'SWAP':
            move = ' '.join([self.pktool(i, 1) for i in move])
        self.printf(f'--> Output: {move}')
        

    def yixin(self, opening, time_in, engine):
        init(engine, self.scrt)
        put('INFO timeout_turn ' + str(time_in * 1000))
        put('INFO timeout_match ' + str(time_in * 1000))
        put('INFO time_left ' + str(time_in * 1000))
        put('INFO max_node 500000000')  # Level 10
        put('INFO max_depth 225')
        put('INFO caution_factor 4')
        put('INFO thread_num 8')  # Set thread
        put('INFO thread_split_depth 20')
        put(f'INFO hash_size {1024 ** 2 * self.memory}')
        put('INFO pondering 0')
        put('INFO vcthread 0')  # Maybe Global Search
        put('INFO rule 1')
        put('START 15 15')
        put('yxboard')
        for i in range(len(opening)):
            if len(opening) % 2 == i % 2:
                put(opening[i] + ',1')
            else:
                put(opening[i] + ',2')
            time.sleep(0.1)
        put('done')
        put('yxswap2step2')
        move = sp_yixin().split()
        kill_engine()
        if move != 0:
            move = ' '.join([self.pktool(i, 1) for i in move])
            printf(f'--> Output: {move}')

    def execute(self):
        opening = self.opening.split()
        try:
            lst = [self.pktool(i, 0) for i in opening]
        except:
            self.printf('An error occur while convert opening to Piskvork coord.')
            return
        if 'GOMOCUP' in self.protocol.upper():
            self.gomocup(lst, self.time, self.engine)
        elif 'YIXIN' in self.protocol.upper():
            self.yixin(lst, self.time, self.engine)
