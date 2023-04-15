from PyQt6.QtWidgets import *
from PyQt6 import uic
from .app import App

class Window(QMainWindow):
    '''GUI of my application'''
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("components/mainwindow.ui", self)
        self.show()
        
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
        
    def slide_rating(self):
        print("Slid the 'rating' slider")