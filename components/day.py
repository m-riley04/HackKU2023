import datetime

class Day:
    def __init__(self, date=datetime.date.today(), time=datetime.datetime.now().strftime("%H:%M:%S"), rating:int=10, emotions:list=[], entries:list=[], imagePath:str=""):
        self.date       = date
        self.time       = time
        self.rating     = rating
        self.emotions   = emotions
        self.entries    = entries
        self.imagePath  = imagePath