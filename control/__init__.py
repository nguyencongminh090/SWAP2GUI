from control.connect import *


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
        if move != 'SWAP':
            move = ' '.join([self.pktool(i, 1) for i in move])
        self.printf(f'--> Output: {move}')
        kill_engine()

    def yixin(self, opening, time_in, engine):
        pass

    def execute(self):
        opening = self.opening.split()
        lst = []
        try:
            lst = [self.pktool(i, 0) for i in opening]
        except:
            self.printf('An error occur while convert opening to Piskvork coord.')
            return
        if 'GOMOCUP' in self.protocol.upper():
            self.gomocup(lst, self.time, self.engine)
        elif 'YIXIN' in self.protocol.upper():
            self.yixin(self.opening, self.time, self.engine)
