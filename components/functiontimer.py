from threading import Timer
class FunctionTimer():
    '''Repeats a function based on a passed time interval'''
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False

    def _run(self):
        '''Auto-starts the timer'''
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        '''Starts the timer'''
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        '''Stops the timer'''
        self._timer.cancel()
        self.is_running = False