import datetime

class Day:
    def __init__(self, date=datetime.date.today(), time=datetime.datetime.now().strftime("%H:%M:%S"), rating:int=10, emotions:list=[], entries:list=[], imagePath:str=""):
        self.date       = date
        self.time       = time
        self.rating     = rating
        self.emotions   = emotions
        self.entries    = entries
        self.imagePath  = imagePath
        
    def info(self):
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Rating: {self.rating}")
        print(f"Emotions: {self.emotions}")
        print(f"Entries: {self.entries}")
        print(f"Image Path: {self.imagePath}")
        return (self.date, self.time, self.rating, self.emotions, self.entries, self.imagePath)