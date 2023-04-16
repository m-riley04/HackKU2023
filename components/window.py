from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtGui import QFontDatabase, QIcon, QPixmap, QAction
from .app import App

class Window(QMainWindow):
    '''GUI of my application'''
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("components/mainwindow.ui", self)
        
        # Window Attributes
        self.appIcon = QIcon('components/icons/icon.ico')
        self.setWindowTitle("ZenLog")
        self.setWindowIcon(self.appIcon)
        self.setFixedSize(800, 588)
        
        # Import Fonts
        QFontDatabase.addApplicationFont("components/stylesheets/fonts/Abel-Regular.ttf")
        QFontDatabase.addApplicationFont("components/stylesheets/fonts/Cinzel-VariableFont_wght.ttf")
        
        # Import Stylesheet
        with open("components/stylesheets/stylesheet.qss", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
            
        # Import Images
        iconPixmap = QPixmap("components/icons/icon.png")
        self.app_logo_pix.setScaledContents(True)
        self.app_logo_pix.setPixmap(iconPixmap)
            
        # Initialize App (the brain) and other temporary variables
        self.app = App()
        self._tempEmotions = []
        
        # Connect Buttons
        self._initialize_widgets()
        self._initialize_tray_icon()
        
        # Show Window
        self.show()
    
    def _initialize_widgets(self):
        '''Initializes the widgets of the app and connects them to their respective commands'''
        self.pages_stack.setCurrentWidget(self.page_myDay)
        
        #-- Top Menu Buttons
        self.btn_myDay.clicked.connect(self.click_myDay)
        self.btn_graphing.clicked.connect(self.click_graphing)
        self.btn_settings.clicked.connect(self.click_settings)
        self.btn_help.clicked.connect(self.click_help)
        self.btn_resources.clicked.connect(self.click_resources)
        
        #-- My Day page
        if self.app.get_submitted() == True:
            self.update_todaysLog()
            self.substack_myDay.setCurrentWidget(self.subpage_log)
            self.set_enabled_widget(self.submenu_myDay, True)
            
        self.btn_todaysLog.clicked.connect(self.click_todaysLog)
        self.btn_addEntry.clicked.connect(self.click_addEntry)
        self.btn_edit.clicked.connect(self.click_edit)
        self.btn_submit.clicked.connect(self.click_submit)
        self.btn_save.clicked.connect(self.click_save)
        self.slider_rating.valueChanged.connect(self.slide_rating)
        self.slider_editRating.valueChanged.connect(self.slide_editRating)
        self.lineEntry_emotion.textChanged.connect(self.typed_emotion)
        self.lineEntry_emotion.returnPressed.connect(self.enterPressed_emotion)
        self.entry_log.textChanged.connect(self.typed_log)
        self.spin_severity.valueChanged.connect(self.spun_severity)
        self.spin_editSeverity.valueChanged.connect(self.spun_editSeverity)
        self.list_logEntries.itemDoubleClicked.connect(self.click_logEntry)
        self.list_logEmotions.itemDoubleClicked.connect(self.click_logEmotion)
        self.btn_publish.clicked.connect(self.click_publish)
        self.lineEntry_editEmotion.textChanged.connect(self.typed_editEmotion)
        self.lineEntry_editEmotion.returnPressed.connect(self.enterPressed_editEmotion)
        
        #-- Graphing page
        self.btn_type.clicked.connect(self.clicked_type)
        self.btn_graph.clicked.connect(self.clicked_graph)
        self.btn_graphType_bar.clicked.connect(self.clicked_graphType_bar)
        self.btn_graphType_line.clicked.connect(self.clicked_graphType_line)
        self.btn_graphType_scatter.clicked.connect(self.clicked_graphType_scatter)
        
        #-- Settings page
        self.btn_colors.clicked.connect(self.click_colors)
        self.btn_general.clicked.connect(self.click_general)
        self.btn_resetUserData.clicked.connect(self.click_resetUserData)
        self.btn_resetToDefaults.clicked.connect(self.click_resetToDefaults)
        self.btn_applyChanges.clicked.connect(self.click_applyChanges)
        
        #-- Help page
        
        #-- Resources page
        
    def _initialize_tray_icon(self):
        '''Initializes the tray icon and it's commands'''
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(self.appIcon)
        
        show_action = QAction("Show", self)
        hide_action = QAction("Hide", self)
        exit_action = QAction("Exit", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        exit_action.triggered.connect(QApplication.quit)
        
        #-- Menu
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(exit_action)
        self.trayIcon.setContextMenu(tray_menu)
        self.trayIcon.show()
        
    #-- Event Overrides
    def closeEvent(self, event):
        event.ignore()
        self.hide()
        self.trayIcon.showMessage(
            "ZenLog",
            "ZenLog was minimized to the tray."
        )
        
    #-- Helpers
    def set_enabled_widget(self, parent, enabled):
        '''Sets the a parent widget and all of it's children to enabled or disabled'''
        parent.setEnabled(enabled)
        for child in parent.findChildren(QPushButton):
            child.setEnabled(enabled)
            
    def update_todaysLog(self):
        '''Updates the Log page of My Day'''
        self.list_logEmotions.clear()
        self.list_logEntries.clear()
        self.substack_myDay.setCurrentWidget(self.subpage_log)
        
        # Update the rating
        self.label_logRating.setText(str(self.app.get_rating()))
        
        # Populate Emotions
        print(self.app.get_emotions())
        for emotion in self.app.get_emotions():
            self.list_logEmotions.addItem(emotion.name)
        
        # Populate Entries
        print(self.app.get_entries())
        for entry in self.app.get_entries():
            self.list_logEntries.addItem(entry.time)
    
    #-- Button Commands --------------------------------
    def click_myDay(self):
        print("Clicked 'My Day'")
        self.pages_stack.setCurrentWidget(self.page_myDay)
        
        if self.app.get_submitted() == True:
            self.submenu_myDay.setEnabled(True)
    
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
        
    def click_logEntry(self):
        print(f"Clicked 'Log Entry' for {list(self.list_logEntries.selectedItems())[0].text()}")
        _entry = self.app.find_entry(list(self.list_logEntries.selectedItems())[0].text())
        popup = QMessageBox(text=_entry.content)
        popup.setWindowTitle(_entry.time)
        popup.exec()
        
    def click_logEmotion(self):
        print(f"Clicked 'Log Emotion' for {list(self.list_logEmotions.selectedItems())[0].text()}")
        _emotion = self.app.find_emotion(list(self.list_logEmotions.selectedItems())[0].text())
        popup = QMessageBox(text=f"Emotion: '{_emotion.name}'\nSeverity: {_emotion.severity}")
        popup.setWindowTitle(_emotion.name)
        popup.exec()
        
    def click_todaysLog(self):
        print("Clicked 'Todays Log'")
        self.update_todaysLog()
        
    def click_addEntry(self):
        print("Clicked 'Add Entry'")
        self.substack_myDay.setCurrentWidget(self.subpage_addEntry)
    
    def click_edit(self):
        print("Clicked 'Edit'")
        self.list_editEmotions.clear()
        self._tempEmotions = []
        for emotion in self.app.get_emotions():
            self._tempEmotions.append(emotion)
            self.list_editEmotions.addItem(emotion.name)
        self.slider_editRating.setValue(self.app.get_rating())
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
        self.update_todaysLog()
        self.set_enabled_widget(parent=self.submenu_myDay, enabled=True)
        self.substack_myDay.setCurrentWidget(self.subpage_thanks)
        
    def click_publish(self):
        print("Clicked 'Publish'")
        self.app.add_log_entry(text=self.entry_newEntry.toPlainText())
        self.update_todaysLog()
        self.substack_myDay.setCurrentWidget(self.subpage_log)
        self.app.save()
         
    def click_save(self):
        print("Clicked 'Save'")
        rating = self.slider_editRating.value()
        emotions = self._tempEmotions
        self.app.set_rating(rating=rating)
        self.app.set_emotions(emotions=emotions)
        self.update_todaysLog()
        self.substack_myDay.setCurrentWidget(self.subpage_log)
        self.app.save()
        
    def click_colors(self):
        print("Clicked 'Colors'")
        self.substack_settings.setCurrentWidget(self.subpage_colors)
        
    def click_general(self):
        print("Clicked 'General'")
        self.substack_settings.setCurrentWidget(self.subpage_general)
        
    def click_applyChanges(self):
        print("Clicked 'Apply Changes'")
        self.app.apply_settings()
        
    def click_resetToDefaults(self):
        print("Clicked 'Resest to Defaults'")
        
        # Double check with user to confirm
        reply = QMessageBox.question(self, "Are you sure you want to reset your settings to default?", "", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.app.reset_settings()
            self.app.apply_settings()
        
    def click_resetUserData(self):
        print("Clicked 'Reset User Data'")
        
        # Double check with user to confirm
        reply = QMessageBox.question(self, "Are you sure you want to reset your user data?", "This will delete ALL recorded days and media.", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.app.reset_data()
            self.substack_myDay.setCurrentWidget(self.subpage_newDay)
            self.submenu_myDay.setEnabled(False)
        
    def clicked_type(self):
        print("Clicked 'Type'")
        
    def clicked_graph(self):
        print("Clicked 'Graph'")
        self.app.graph_data()
        
    def clicked_graphType_bar(self):
        print("Clicked 'Graph Type - Bar'")
        self.app.set_grapher()
        self.app.set_grapher_type(type="bar")
        self.btn_graph.setEnabled(True)
        
    def clicked_graphType_line(self):
        print("Clicked 'Graph Type - Line'")
        self.app.set_grapher()
        self.app.set_grapher_type(type="line")
        self.btn_graph.setEnabled(True)
        
    def clicked_graphType_scatter(self):
        print("Clicked 'Graph Type - Scatter'")
        self.app.set_grapher()
        self.app.set_grapher_type(type="scatter")
        self.btn_graph.setEnabled(True)
        
    #-- Slider Commands --------------------------------
    def slide_rating(self):
        print(f"Slid the 'rating' slider to {self.slider_rating.value()}")
        
    def slide_editRating(self):
        print(f"Slid the 'edit rating' slider to {self.slider_editRating.value()}")
        
    #-- Typed Commands --------------------------------
    def typed_emotion(self):
        print("Typed in the 'emotion' text field")
        
    def typed_editEmotion(self):
        print("Typed in the 'edit emotion' text field")
        
    def typed_log(self):
        print("Typed in the 'log' textbox")
        
    def typed_newEntry(self):
        print("Typed in the 'new entry' textbox")
        
    #-- Enter Commands --------------------------------
    def enterPressed_emotion(self):
        print("'Enter' hit in the 'emotions' text field")
        if self.lineEntry_emotion.text() == "":
            message = QMessageBox()
            print("Error")
            message.setText("ERROR: Emotion does not have a name!")
            message.exec()
            return
        name = self.lineEntry_emotion.text()
        severity = self.spin_severity.value()
        self._tempEmotions.append(self.app.create_emotion(name=name, severity=severity))
        self.list_emotions.addItem(name)
        self.lineEntry_emotion.clear()
        self.spin_severity.setValue(1)
        
    def enterPressed_editEmotion(self):
        print("'Enter' hit in the 'edit emotions' text field")
        if self.lineEntry_editEmotion.text() == "":
            message = QMessageBox()
            print("Error")
            message.setText("ERROR: Emotion does not have a name!")
            message.exec()
            return
        name = self.lineEntry_editEmotion.text()
        severity = self.spin_editSeverity.value()
        self._tempEmotions.append(self.app.create_emotion(name=name, severity=severity))
        self.list_editEmotions.addItem(name)
        self.lineEntry_editEmotion.clear()
        self.spin_editSeverity.setValue(1)
        
    #-- Spinners Commands ------------------------------
    def spun_severity(self):
        print("Spun the 'severity' spinner")
        
    def spun_editSeverity(self):
        print("Spun the 'Edit Serverity' spinner")