import plyer
import os

ICON_PATH = f"{os.getcwd()}/components/icons/icon.ico"
print(ICON_PATH)
APP_NAME = "ZenLog"

class Notifier:
    def __init__(self):
        pass
    
    def notify(self, title, message, timeout=10, icon=ICON_PATH):
        '''Displays a notification with a title, message, and icon'''
        plyer.notification.notify(title=title, message=message, app_icon=icon, timeout=timeout)