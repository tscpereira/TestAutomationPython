import datetime


def message(message):
    print("[" + str(datetime.datetime.today().strftime('%d/%m/%Y %H:%M:%S')) + "] - " + message)
