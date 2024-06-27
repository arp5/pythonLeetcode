class HitCounter:

    def __init__(self):
        self.queue = []

    def hit(self, timestamp: int) -> None:
        while self.queue and (timestamp-self.queue[0][0]) > 300:
            self.queue.pop(0)
        if self.queue and self.queue[-1][0] == timestamp:
            t,r = self.queue.pop()
            self.queue.append((t,r+1))
        else:
            self.queue.append((timestamp,1))
        print(self.queue)

    def getHits(self, timestamp: int) -> int:
        n = 0
        while self.queue and (timestamp-self.queue[0][0])>=300:
            t,r = self.queue.pop(0)
        for t,r in self.queue:
            n+=r
        return n


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)