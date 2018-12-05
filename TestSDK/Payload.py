import json


class Payload(object):

    def __init__(self, j):
        self.__dict__ = json.loads(j)
