import datetime

class LogEntry:
    def __init__(self, content, time=datetime.datetime.now().strftime("%I:%M:%S %p"), date=str(datetime.date.today())):
        self.content    = content
        self.time       = time
        self.date       = date