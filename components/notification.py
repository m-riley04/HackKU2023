class Notification:
    def __init__(self, title="Notification Title", message="This is a default notification message.", imagePath="", onNotify=None):
        self.title = title
        self.message = message
        self.imagePath = imagePath
        self.onNotify = onNotify