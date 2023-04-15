import datetime

class LogEntry:
    def __init__(self, content, time=datetime.datetime.now().strftime("%I:%M:%S %p")):
        self.content    = content
        self.time       = time