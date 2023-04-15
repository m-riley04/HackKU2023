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
        if self.app.get_submitted() == True:
            self.substack_myDay.setCurrentWidget(self.subpage_thanks)
        self.btn_addEntry.clicked.connect(self.click_addEntry)
        self.btn_edit.clicked.connect(self.click_edit)
        self.btn_submit.clicked.connect(self.click_submit)
        self.slider_rating.valueChanged.connect(self.slide_rating)
        self.lineEntry_emotion.textChanged.connect(self.typed_emotion)
        self.lineEntry_emotion.returnPressed.connect(self.enterPressed_emotion)
        self.entry_log.textChanged.connect(self.typed_log)
        self.spin_severity.valueChanged.connect(self.spun_severity)
        
        #-- Graphing page
        
        #-- Settings page
        self.btn_colors.clicked.connect(self.click_colors)
        self.btn_notifications.clicked.connect(self.click_notifications)
        self.btn_resetUserData.clicked.connect(self.click_resetUserData)
        self.btn_applyChanges.clicked.connect(self.click_applyChanges)
        
        #-- Help page
        
        #-- Resources page
    
    def click_myDay(self):
        print("Clicked 'My Day'")
        self.pages_stack.setCurrentWidget(self.page_myDay)
    
    def click_graphing(self):
        print("Clicked 'Graphing'")
        self.pages_stack.setCurrentWidget(self.page_graphing)
    
    def click_settings(self):
        print("Clicked 'Settings'")
        self.pages_stack.setCurrentWidget(self.page_settings)
    
    def click_help(self):
        print("Clicked 'Help'")
        self.pages_stack.setCurrentWidget(self.page_help)
    
    def click_resources(self):
        print("Clicked 'Resources'")
        self.pages_stack.setCurrentWidget(self.page_resources)
        
    def click_addEntry(self):
        print("Clicked 'Add Entry'")
        self.substack_myDay.setCurrentWidget(self.subpage_log)
    
    def click_edit(self):
        print("Clicked 'Edit'")
        self.substack_myDay.setCurrentWidget(self.subpage_edit)
        
    def click_submit(self):
        print("Clicked 'Submit'")
        rating = self.slider_rating.value()
        emotions = self._tempEmotions
        log = self.entry_log.toPlainText()
        self.app.set_rating(rating=rating)
        self.app.set_emotions(emotions=emotions)
        self.app.add_log_entry(text=log)
        self.app.get_day().info()
        self.app.set_submitted(submitted=True)
        self.app.save()
        self.btn_edit.setEnabled(True)
        self.btn_addEntry.setEnabled(True)
        self.substack_myDay.setCurrentWidget(self.subpage_thanks)
        
    def click_colors(self):
        print("Clicked 'Colors'")
        
    def click_notifications(self):
        print("Clicked 'Notifications'")
        
    def click_applyChanges(self):
        print("Clicked 'Apply Changes'")
        
    def click_resetToDefault(self):
        print("Clicked 'Resest to Defaults'")
        
    def click_resetUserData(self):
        print("Clicked 'Reset User Data'")
        
        
    def slide_rating(self):
        print(f"Slid the 'rating' slider to {self.slider_rating.value()}")
        
    def typed_emotion(self):
        print("Typed in the 'emotion' text field")
        
    def typed_log(self):
        print("Typed in the 'log' textbox")
        
    def enterPressed_emotion(self):
        print("'Enter' hit in the 'emotions' text field")
        name = self.lineEntry_emotion.text()
        severity = self.spin_serverity.value()
        self._tempEmotions.append(self.app.create_emotion(name=name, severity=severity))
        self.list_emotions.addItem(name)
        self.lineEntry_emotion.clear()
        
    def spun_severity(self):
        print("Spun the 'severity' spinner")