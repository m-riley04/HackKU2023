import datetime

class LogEntry:
    def __init__(self, content, time=datetime.datetime.now().strftime("%H:%M:%S"), ):
        self.content    = content
        self.time       = time