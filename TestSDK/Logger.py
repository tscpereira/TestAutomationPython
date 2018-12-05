# encoding: utf-8

import sys

_path = None


class Logger(object):
    def __init__(self, path):
        self._path = path
        self.terminal = sys.stdout
        self.log = open(self._path + "\\TestLog.txt", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def close(self):
        self.log.close()
