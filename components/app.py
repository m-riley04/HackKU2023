from .logentry import LogEntry
from .emotion import Emotion, COMMON_EMOTIONS
from .day import Day
import json

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
    
    def add_log_entry(self, text):
        newEntry = LogEntry(content=text)
        self.day.entries.append(newEntry)
        
    def add_emotion(self, emotion):
        self.day.emotions.append(emotion)
        
    def create_emotion(self, name, severity=1):
        return Emotion(name=name, severity=severity)
        
    def set_rating(self, rating):
        self.day.rating = rating
        
    def set_emotions(self, emotions):
        self.day.emotions = emotions
        
    def get_common_emotions(self):
        return COMMON_EMOTIONS
        
    def get_day(self):
        return self.day
    
    def get_emotions(self):
        return self.day.emotions
    
    def get_rating(self):
        return self.day.rating
    
    def get_entries(self):
        return self.day.entries
    
    def get_imagePath(self):
        return self.day.imagePath