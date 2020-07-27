from threading import Timer

class RepeatedTimer(object):
    def __init__(self, interval, counter, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.counter    = 0
        self.limit      = counter
        self.start()

    def _run(self):
        self.is_running = False
        if self.counter < self.limit:
            self.counter = self.counter + 1
            self.start()
            self.function(*self.args, **self.kwargs)
        else:
            self.stop()

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False

