from .logentry import LogEntry
from .day import Day

class App:
    def __init__(self):
        self.day = None
        
        self.set_current_day()
    
    def set_current_day(self):
        #TODO: Add changing day
        self.day = Day()
        return self.day
    
    def save_day(self):
        pass
    
    def add_entry(self, text):
        newEntry = LogEntry(content=text)
        self.day.entries.append(newEntry)