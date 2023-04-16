from PyQt6.QtWidgets import *
from PyQt6.QtCore import QBitArray
from PyQt6 import uic
from PyQt6.QtGui import QFontDatabase, QIcon, QPixmap, QAction
from .app import App
import os

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
        
        # Initialize Objects/Widgets
        self._initialize_widgets()
        self._initialize_tray_icon()
        self._initialize_toolbar()
        
        # Show Window
        self.show()
    
    def _initialize_widgets(self):
        '''Initializes the widgets of the app and connects them to their respective commands'''
        self.pages_stack.setCurrentWidget(self.page_myDay)
        
        #-- Navigation Buttons
        self.btn_myDay.clicked.connect(self.click_myDay)
        self.btn_graphing.clicked.connect(self.click_graphing)
        self.btn_settings.clicked.connect(self.click_settings)
        self.btn_help.clicked.connect(self.click_help)
        self.btn_resources.clicked.connect(self.click_resources)
        
        #-- Submenu Buttons
        self.btn_todaysLog.clicked.connect(self.click_todaysLog)
        self.btn_addEntry.clicked.connect(self.click_addEntry)
        self.btn_edit.clicked.connect(self.click_edit)
        self.btn_allLogs.clicked.connect(self.click_allLogs)
        self.btn_allPictures.clicked.connect(self.click_allPictures)
        self.btn_type.clicked.connect(self.click_type)
        self.btn_graph.clicked.connect(self.click_graph)
        self.btn_colors.clicked.connect(self.click_colors)
        self.btn_general.clicked.connect(self.click_general)
        self.btn_resetUserData.clicked.connect(self.click_resetUserData)
        self.btn_helpMyDay.clicked.connect(self.click_helpMyDay)
        self.btn_helpGraphing.clicked.connect(self.click_helpGraphing)
        self.btn_helpResources.clicked.connect(self.click_helpResources)
        self.btn_contacts.clicked.connect(self.click_contacts)
        self.btn_facilities.clicked.connect(self.click_facilities)
        self.btn_treatment.clicked.connect(self.click_treatment)
        self.btn_dsm5.clicked.connect(self.click_dsm5)
        
        #-- Other Buttons
        self.btn_submit.clicked.connect(self.click_submit)
        self.btn_save.clicked.connect(self.click_save)
        self.btn_publish.clicked.connect(self.click_publish)
        self.btn_graphType_bar.clicked.connect(self.click_graphType_bar)
        self.btn_graphType_line.clicked.connect(self.click_graphType_line)
        self.btn_graphType_scatter.clicked.connect(self.click_graphType_scatter)
        self.btn_resetToDefaults.clicked.connect(self.click_resetToDefaults)
        self.btn_applyChanges.clicked.connect(self.click_applyChanges)
        self.btn_dsm5Link.clicked.connect(self.click_dsm5Link)
        
        #-- Sliders
        self.slider_rating.valueChanged.connect(self.slide_rating)
        self.slider_editRating.valueChanged.connect(self.slide_editRating)
        
        #-- Incremnet Spinners
        self.spin_severity.valueChanged.connect(self.spun_severity)
        self.spin_editSeverity.valueChanged.connect(self.spun_editSeverity)
        
        #-- Item Lists
        self.list_logEntries.itemDoubleClicked.connect(self.click_logEntry)
        self.list_logEmotions.itemDoubleClicked.connect(self.click_logEmotion)
        
        #-- Line Entry
        self.lineEntry_emotion.textChanged.connect(self.typed_emotion)
        self.lineEntry_emotion.returnPressed.connect(self.enterPressed_emotion)
        self.lineEntry_editEmotion.textChanged.connect(self.typed_editEmotion)
        self.lineEntry_editEmotion.returnPressed.connect(self.enterPressed_editEmotion)
        
        #-- Text Entry
        self.entry_log.textChanged.connect(self.typed_log)
        
        #-- My Day page
        if self.app.get_submitted() == True:
            self.update_todaysLog()
            self.substack_myDay.setCurrentWidget(self.subpage_log)
            self.set_enabled_widget(self.submenu_myDay, True)
        
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
        
    def _initialize_toolbar(self):
        '''Initializes the toolbar and all it's commands'''
        self.actionSave.triggered.connect(self.action_save)
        self.actionLoad.triggered.connect(self.action_load)
        self.actionExport.triggered.connect(self.action_export)
        self.actionOpenFolder.triggered.connect(self.action_openFolder)
        self.actionReset.triggered.connect(self.action_reset)
        
    #-- Event Overrides
    def closeEvent(self, event):
        if self.app.get_settings()["general"]["minimize-to-tray"] != False:
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
        for emotion in self.app.get_emotions():
            self.list_logEmotions.addItem(emotion.name)
        
        # Populate Entries
        for entry in self.app.get_entries():
            self.list_logEntries.addItem(entry.time)
    
    #-- Toolbar Commands --------------------------------
    def action_save(self):
        '''Saves the current day'''
        self.app.save()
    
    def action_load(self):
        '''Loads a JSON file into the database and overwrites the current JSON'''
        reply = QMessageBox.question(self, "Load Data", "Are you sure you want to load? This will overwrite any current data.", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            dataPath = QFileDialog.getOpenFileName(self, "Open", "", "JSON (*.json)")[0]
            if dataPath == "":
                message = QErrorMessage(self)
                message.showMessage("ERROR: Data load operation cancelled.")
                message.exec()
                return
            self.app.load_data(dataPath)
            self.app.load()
            if not self.app.get_submitted():
                self.substack_myDay.setCurrentWidget(self.subpage_newDay)
                self.submenu_myDay.setEnabled(False)
            else:
                self.substack_myDay.setCurrentWidget(self.subpage_log)
                self.set_enabled_widget(self.submenu_myDay, True)
    
    def action_export(self):
        '''Exports the current JSON file into a directory of the user's choice'''
        path = QFileDialog.getSaveFileName(self, "Export", "", "JSON (*.json)")[0]
        if path != "":
            try:
                return self.app.export(path)
            except FileExistsError:
                message = QErrorMessage(self)
                message.showMessage("ERROR: A file of the same name already exists there. Please choose another directory.")
                message.exec()
            except:
                message = QErrorMessage(self)
                message.showMessage("ERROR: An unknown error occurred while exporting. Please try again.")
                message.exec()
    
    def action_openFolder(self):
        '''Opens the root folder of the application'''
        pass
    
    def action_reset(self):
        '''Prompts the user if they want to reset all their user data. Resets it if they select "Yes"'''
        reply = QMessageBox.question(self, "Reset User Data", "Are you sure you want to reset your user data? This will delete ALL recorded days and media.", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.app.reset_data()
            self.app.load()
            self.substack_myDay.setCurrentWidget(self.subpage_newDay)
            self.submenu_myDay.setEnabled(False)
    
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
        
    def click_allLogs(self):
        print("Clicked 'All Logs'")
        
    def click_allPictures(self):
        print("Clicked 'All Pictures'")
        self.app.open_path(rf'{os.getcwd()}\media')
        
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
        
    def click_type(self):
        print("Clicked 'Type'")
        
    def click_graph(self):
        print("Clicked 'Graph'")
        self.app.graph_data()
        
    def click_graphType_bar(self):
        print("Clicked 'Graph Type - Bar'")
        self.app.set_grapher()
        self.app.set_grapher_type(type="bar")
        self.btn_graph.setEnabled(True)
        
    def click_graphType_line(self):
        print("Clicked 'Graph Type - Line'")
        self.app.set_grapher()
        self.app.set_grapher_type(type="line")
        self.btn_graph.setEnabled(True)
        
    def click_graphType_scatter(self):
        print("Clicked 'Graph Type - Scatter'")
        self.app.set_grapher()
        self.app.set_grapher_type(type="scatter")
        self.btn_graph.setEnabled(True)
        
    def click_helpMyDay(self):
        print("Clicked 'Help My Day'")
    
    def click_helpGraphing(self):
        print("Clicked 'Help Graphing'")
    
    def click_helpResources(self):
        print("Clicked 'Help Resources'")
    
    def click_contacts(self):
        print("Clicked 'Contacts'")
    
    def click_facilities(self):
        print("Clicked 'Facilities'")
    
    def click_treatment(self):
        print("Clicked 'Treatment'")
    
    def click_dsm5(self):
        print("Clicked 'DSM5'")
    
    def click_dsm5Link(self):
        print("Clicked 'DSM-5 Link'")
        
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