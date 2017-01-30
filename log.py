import sys

class Log(object):
    def __init__(self, logfile=None):
        if logfile is None:
            self.out = sys.stdout
        else:
            self.out = open('log.txt', 'a')

    def msg(self, msg):
        try:
            self.out.write(msg + '\n')
        except Exception as e:
            self.out.write(e.msg + '\n')
