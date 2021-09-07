from control import *


class Control:
    def __init__(self, opening: str, time, engine, protocol, scrt):
        self.opening = opening
        self.time = time
        self.engine = engine
        self.protocol = protocol
        self.scrt = scrt

    def printf(self, *txt, endl='\n'):
        try:
            txt = [str(i) for i in txt]
            self.scrt.insert('insert', ' '.join(txt) + endl)
        except:
            pass

    def execute(self):
        opening = self.opening.split()
        lst = []
        try:
            for i in opening:
                x = str(ord(i[:1]) - 97)
                y = str(int(i[1:]) - 1)
                lst.append(x + ',' + y)
        except:
            self.printf('An error occur while convert opening to Piskvork coord.')
            return
        # Show opening after convert
        for i in lst:
            self.printf(i, endl=' ')
        pass
