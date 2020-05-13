
# First attempt, O(n) space and time
class RecentCounter:

    def __init__(self):
        self.ping_queue = []

    def ping(self, t: int) -> int:
        cutoff_time = t - 3000
        while self.ping_queue and self.ping_queue[0] < cutoff_time:
            self.ping_queue.pop(0)
        self.ping_queue.append(t)
        return len(self.ping_queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)