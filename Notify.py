import threading
from datetime import datetime

# priority constants
HIGH = 1
LOW = 0


class Notify(threading.Thread):
    """ Notify class. Responsible for managing notifications time management
    
        Low priority breaks don't affect how long you need to wait for another
        break. 
        
        High priority breaks reset the time needed for the next break.
    """

    def __init__(self, interval=10,
                 duration=5, name=None,
                 priority=LOW):
        # class constructor
        threading.Thread.__init__(self)
        self.event = threading.Event()
        self.interval = interval
        self.duration = duration
        self.name = name
        self.count = self.interval
        self.priority = priority

    def notify(self):
        # add notification procedures here
        print(str(datetime.now())
              + " - Time to: " + self.name
              + " - Duration: " + str(self.duration))

    def run(self):
        # main thread method
        self.counter(self.interval)
        self.notify()
        if self.priority == HIGH:
            for notifier in notifiers:
                notifier.stop()
        self.counter(self.duration)
        if self.priority == HIGH:
            for notifier in notifiers:
                notifier.run()
        else:
            self.run()

    def counter(self, number):
        # this method waits number seconds
        while number > 0 and not self.event.is_set():
            number -= 1
            self.event.wait(1)

    def stop(self):
        # this method pauses the thread
        self.event.set()


testbreak = Notify(10, 5, "ay", HIGH)
testbreak.start()
notifiers = [testbreak]
