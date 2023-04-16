import notify2

ICON_PATH = "icons/icon.png"
APP_NAME = "ZenLog"

class Notifier:
    def __init__(self):
        # Initialize notify2 with app name
        notify2.init(APP_NAME)
        
        # Create notification object
        self.notification = None
    
    def notify(self, title, message, urgency=2, timeout=True, icon=ICON_PATH):
        '''Displays a notification with a title, message, and icon'''
        self.notification = notify2.Notification(title, message, icon)
        self.set_urgency(urgency)
        self.set_timeout(timeout)
        self.notification.show()
        
    def set_icon(self, icon):
        '''Sets the notification icon'''
        self.notification.icon = icon
        
    def set_title(self, title):
        '''Sets the notification title'''
        self.notification.summary = title
        
    def set_message(self, message):
        '''Sets the notification messsage'''
        self.notification.message = message
    
    def set_urgency(self, urgency:int=2):
        '''
        Sets the notification urgency state.
        1. URGENCY_LOW
        2. URGENCY_NORMAL
        3. URGENCY_CRITICAL
        '''
        if urgency == 1:
            self.notification.set_urgency(notify2.URGENCY_LOW)
        elif urgency == 2:
            self.notification.set_urgency(notify2.URGENCY_NORMAL)
        elif urgency == 3:
            self.notification.set_urgency(notify2.URGENCY_CRITICAL)
        else:
            raise ValueError("Not a number between 1 and 3")
        
    def set_timeout(self, timeout=True):
        '''Set the notification timeout in seconds'''
        if timeout == False:
            self.notification.set_timeout(notify2.EXPIRES_NEVER)
        elif timeout == True:
            self.notification.set_timeout(notify2.EXPIRES_DEFAULT)
        else:
            self.notification.set_timeout((timeout//1000))
    