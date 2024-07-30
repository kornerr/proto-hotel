import time
from cld import *

class desktop_Timer():
    def __init__(self):
        self.callback = None
        self.queue = []
        self.reportQueue = []

    # Only remove one item per execution, because it's enough
    def removeObsolete(self):
        n = cld_len(self.queue)
        for i in range(0, n):
            item = self.queue[i]
            if item[0] == 0:
                del self.queue[i]
                return

    def report(self):
        q = self.reportQueue
        self.reportQueue = []
        n = cld_len(q)
        for i in range(0, n):
            key = q[i][0]
            value = q[i][1]
            self.callback(key, value)

    def schedule(self, key, value, timeout):
        # Get current time in milliseconds.
        now = time.time_ns() // 1000000
        self.queue.append([now + timeout, key, value])

    def scheduleReporting(self):
        # Get current time in milliseconds.
        now = time.time_ns() // 1000000

        n = cld_len(self.queue)
        for i in range(0, n):
            item = self.queue[i]
            if (
                item[0] > 0 and
                now >= item[0]
            ):
                # Mark for removal.
                item[0] = 0
                key = item[1]
                value = item[2]
                self.reportQueue.append([key, value])

    def update(self):
        self.scheduleReporting()
        self.removeObsolete()
        self.report()
