from PyQt6.QtWidgets import *
from PyQt6 import uic
from .app import App

class Window(QMainWindow):
    '''GUI of my application'''
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("components/mainwindow.ui", self)
        self.show()
        
        self.app = App()
        self._tempEmotions = []
        
        # Connect Buttons
        self._initialize_widgets()
    
    def _initialize_widgets(self):
        #-- Top Menu Buttons
        self.btn_myDay.clicked.connect(self.click_myDay)
        self.btn_graphing.clicked.connect(self.click_graphing)
        self.btn_settings.clicked.connect(self.click_settings)
        self.btn_help.clicked.connect(self.click_help)
        self.btn_resources.clicked.connect(self.click_resources)
        
        #-- My Day page
        self.btn_addEntry.clicked.connect(self.click_addEntry)
        self.btn_changeRating.clicked.connect(self.click_changeRating)
        self.btn_submit.clicked.connect(self.click_submit)
        self.slider_rating.valueChanged.connect(self.slide_rating)
        self.lineEntry_emotion.textChanged.connect(self.typed_emotion)
        self.lineEntry_emotion.returnPressed.connect(self.enterPressed_emotion)
        self.entry_log.textChanged.connect(self.typed_log)
        
        #-- Graphing page
        
        #-- Settings page
        
        #-- Help page
        
        #-- Resources page
    
    def click_myDay(self):
        print("Clicked 'My Day'")
    
    def click_graphing(self):
        print("Clicked 'Graphing'")
    
    def click_settings(self):
        print("Clicked 'Settings'")
    
    def click_help(self):
        print("Clicked 'Help'")
    
    def click_resources(self):
        print("Clicked 'Resources'")
        
    def click_addEntry(self):
        print("Clicked 'Add Entry'")
    
    def click_changeRating(self):
        print("Clicked 'Change Rating'")
        
    def click_submit(self):
        print("Clicked 'Submit'")
        rating = self.slider_rating.tickInterval()
        emotions = self._tempEmotions
        log = self.entry_log.toPlainText()
        self.app.set_rating(rating=rating)
        self.app.set_emotions(emotions=emotions)
        self.app.add_log_entry(text=log)
        self.app.get_day().info()
        
    def slide_rating(self):
        print("Slid the 'rating' slider")
        
    def typed_emotion(self):
        print("Typed in the 'emotion' text field")
        
    def typed_log(self):
        print("Typed in the 'log' textbox")
        
    def enterPressed_emotion(self):
        print("'Enter' hit in the 'emotions' text field")