from .logentry import LogEntry
from .emotion import Emotion, COMMON_EMOTIONS
from .day import Day
from .grapher import Grapher
from .helpers import check_directory
from .functiontimer import FunctionTimer
from .notifier import Notifier
import shutil, os, json, subprocess, random, webbrowser, datetime

#-- Default Databases
SETTINGS_DEFAULT = {
    "notifications-enabled" : True,
    "time-start" : "08:00:00",
    "time-end" : "21:00:00",
    "minimize-to-tray" : True,
    "auto-run" : False
}

DAYS_DEFAULT = { "days" : {} }

class App:
    def __init__(self):
        self._days = {}
        self._settings = {}
        self._nextNotification = ""
        self.day = None
        self.grapher = None
        self.updateTimer = FunctionTimer(5, self.check_time)
        self.notificationManager = Notifier()
        
        #-- Load Schedule
        with open(f"{os.getcwd()}/user_data/schedule.json", "r") as file:
            self._nextNotification = json.loads(file.read())
        
        #-- Load Rest
        self.load()
        
    def check_time(self):
        '''Compares the current time and date with the next scheduled notification times'''
        scheduled = datetime.datetime.strptime(self._nextNotification["next-datetime"], "%m-%d-%YT%H:%M:%S")
        
        if scheduled <= datetime.datetime.now():
            if self._settings["notifications-enabled"] == True:
                self.notificationManager.notify(title="It's time to log! Don't be late!", message="Open ZenLog from the taskbar and let's get healthier together!")
            self.schedule_next()
            
    def visit_website(self, url:str="https://google.com"):
        '''Opens a website from a given URL in the browser'''
        webbrowser.open_new_tab(url)
        
    def schedule_next(self, hourStart, hourEnd):
        '''Randomly schedules the next notification datetime'''
        #TODO
        d = hourEnd - hourStart
        random.randrange(hourStart, hourEnd)

    def dev_notification(self):
        if self._settings["notifications-enabled"] == True:
            self.notificationManager.notify(title="Notification Title", message="This is the notification message.")
    
    def get_settings(self):
        '''Returns a dictionary of the settings for the app'''
        return self._settings
    
    def set_new_day(self):
        '''Sets the new current day'''
        self.day = Day()
        return self.day
    
    def get_date(self):
        '''Returns the date of the current Day'''
        _temp = Day()
        return _temp.date
    
    def find_emotion(self, name):
        '''Searches through the list of emotions for a match in the given name. Returns the first entry that matches, or False if there is no match.'''
        for emotion in self.get_emotions():
            if emotion.name == name:
                return emotion
        return False
    
    def find_entry(self, time, all=False):
        '''Searches through the list of entries for a match in the given time. Returns the first entry that matches, or False if there is no match.'''
        if not all:
            for entry in self.get_entries():
                if entry.time == time:
                    return entry
        else:
                for entry in self.get_all_entries():
                    if entry.time == time:
                        return entry
        return False
    
    def get_all_entries(self) -> list[LogEntry]:
        '''Returns a list of all entries'''
        _temp = []
        for day in self._days.keys():
            for entry in self._days[day]["entries"]:
                _temp.append(LogEntry(content=entry["content"], date=entry["date"], time=entry["time"]))
        return _temp
    
    def open_path(self, path):
        subprocess.Popen(fr'explorer /open, "{path}"')
    
    def save(self):
        '''Saves the current day into the JSON database'''
        # Check for empty day
        if self.day == None:
            return False
        
        currentDate = str(self.get_date())
        self._days[currentDate] = {}
        for key, value in self.day.__dict__.items():
            if type(value) == list:
                _temp = []
                for i in value:
                    _temp.append(i.__dict__)
                value = _temp
                self._days[currentDate][str(key)] = value
            elif type(value) != int and type(value) != bool:
                self._days[currentDate][str(key)] = str(value)
            else:
                self._days[currentDate][str(key)] = value
            
            
        jsonData = json.dumps({"days": self._days}, indent=4)
        
        # Save to file
        _dirPath = f"{os.getcwd()}/user_data"
        check_directory(_dirPath)
        with open(f"{_dirPath}/days.json", "w") as file:
            file.write(jsonData)
        
    def load(self):
        '''Loads the current day and settings from the database. Returns the day if it finds one, otherwise it create a new one.'''
        #-- Load Settings
        _dirPath = f"{os.getcwd()}/user_data"
        check_directory(_dirPath)
        with open(f"{_dirPath}/settings.json", "r") as file:
            self._settings = json.loads(file.read())["settings"]
        
        #-- Load day
        with open(f"{_dirPath}/days.json", "r") as file:
            self._days = json.loads(file.read())["days"]
        
        # Check every day to see if it matches today
        for day in self._days.keys():
            if day == str(self.get_date()):
                
                # Load day emotions
                emotions = []
                for i in self._days[day]["emotions"]:
                    emotions.append(Emotion(i["name"], i["severity"]))
                    
                # Load day entries
                entries = []
                for i in self._days[day]["entries"]:
                    entries.append(LogEntry(i["content"], i["time"], i["date"]))
                
                # Load day
                self.day = Day(date=day, time=self._days[day]["time"], rating=self._days[day]["rating"], emotions=list(emotions), entries=list(entries), imagePath=self._days[day]["imagePath"], submitted=bool(self._days[day]["submitted"]))
                
                return self.day
        
        # If not, set a new day 
        self.set_new_day()
        
    def export(self, path):
        '''Exports all the user's information to a directory of their choice.'''
        try:
            shutil.copy(src=f"{os.getcwd()}/user_data/days.json", dst=path)
        except shutil.SameFileError:
            raise FileExistsError("Duplicate file exists.")
        except:
            raise RuntimeError("Unknown error while exporting.")
        
    def reset_data(self):
        '''Resets the current user's data'''
        
        _dirPath = f"{os.getcwd()}/user_data"
        check_directory(_dirPath)
        with open(f"{_dirPath}/days.json", "w") as file:
            file.write(json.dumps({"days" : {}}))
            
        self.load()
        
    def reset_settings(self):
        '''Resets the current user's settings'''
        check_directory(f"{os.getcwd()}/user_data")
        with open(f"{os.getcwd()}/user_data/settings.json", "w") as file:
            file.write(json.dumps({"settings" : SETTINGS_DEFAULT}, indent=4))

    def repair(self):
        '''Repairs broken data files and directories'''

    def load_data(self, path):
        '''Replaces the current user's data with the given path'''
        try:
            shutil.copy(dst=f"{os.getcwd()}/user_data/days.json", src=path)
        except shutil.SameFileError:
            raise FileExistsError("Duplicate file exists.")
        except:
            raise RuntimeError("Unknown error while exporting.")

    def apply_settings(self, notifications, timeStart, timeEnd, minimize, autoRun):
        '''Applies the current user's selected settings'''
        self._settings["notifications-enabled"] = notifications
        self._settings["time-start"] = timeStart
        self._settings["time-end"] = timeEnd
        self._settings["minimize-to-tray"] = minimize
        self._settings["auto-run"] = autoRun
        
        check_directory(f"{os.getcwd()}/user_data")
        with open(f"{os.getcwd()}/user_data/settings.json", "w") as file:
            file.write(json.dumps({"settings" : self._settings}, indent=4))
        
        self.save()

    def set_grapher(self):
        '''Initializes the grapher object'''
        days = list(self._days.keys())
        yValues = []
        for i in days:
            yValues.append(self._days[i]["rating"])
        self.grapher = Grapher(x=days, y=yValues)
        
    def set_grapher_type(self, type):
        '''Sets the graph type for the grapher'''
        self.grapher.set_graph_type(type=type)
   
    def graph_data(self):
        '''Graphs the data on a chart'''
        if self.grapher == None:
            raise RuntimeError("ERROR: Grapher object is not set.")
        
        self.grapher.plot()
    
    def add_log_entry(self, text):
        '''Adds a log entry to the entries list'''
        newEntry = LogEntry(content=text)
        self.day.entries.append(newEntry)
        
    def add_emotion(self, emotion):
        '''Adds a new emotion to the emotions list'''
        self.day.emotions.append(emotion)
        
    def create_emotion(self, name, severity=1):
        '''Creates a new emotion object'''
        return Emotion(name=name, severity=severity)
        
    def set_rating(self, rating):
        '''Sets the rating'''
        self.day.rating = rating
        
    def set_emotions(self, emotions):
        '''Sets the emotion list'''
        self.day.emotions = emotions
        
    def set_entries(self, entries):
        '''Sets the log entry list'''
        self.day.entries = entries
        
    def set_imagePath(self, path):
        '''Sets the image path'''
        self.day.imagePath = path
        
    def set_submitted(self, submitted):
        '''Sets the submitted flag'''
        self.day.submitted = submitted
        
    def get_common_emotions(self):
        '''Returns a list of common emotions'''
        return COMMON_EMOTIONS
        
    def get_day(self):
        '''Returns the Day object'''
        return self.day
    
    def get_emotions(self):
        '''Returns the list of emotions'''
        return self.day.emotions
    
    def get_rating(self):
        '''Returns the rating'''
        return self.day.rating
    
    def get_entries(self):
        '''Returns the list of log entries'''
        return self.day.entries
    
    def get_imagePath(self):
        '''Returns the image path'''
        return self.day.imagePath
    
    def get_submitted(self):
        '''Returns the submitted flag'''
        return self.day.submitted