# Thread Manager Library for Stanley Solutions

# Import Required Libraries
import time
from threading import Thread, Timer
from subprocess import Popen, PIPE

# Define Repeate Thread Function
class RepeatedThread():
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
    
    def restart(self):
        self.stop()
        self.start()

# Define OS-Interfaced Thread Class
class OsCommand():
    def __init__(self,message,threaded=True,delay=5):
        self.command = message.split()
        self.dly_time = delay
        if threaded:
            t = Thread(target=self.run)
            t.start()
            return
    
    def run(self):
        time.sleep(self.dly_time)
        proc = Popen(self.command, stdin=PIPE, stderr=PIPE, universal_newlines=True)
        response = proc.communicate()[1]
        return(response)

# Define Threaded Operation Class to Handle Independent Function Calls
class CallThread():
    def __init__(self,function,delay=0,*args,**kwargs):
        self.func = function
        self.args = args
        self.kwargs = kwargs
        self.delay  = delay
        Thread(target=self._run).start()
    
    def _run(self):
        time.sleep(self.delay)
        self.func(*self.args,**self.kwargs)