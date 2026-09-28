
class MyCalendar:

    def __init__(self):
        self.segs = []            
    
    def book(self, startTime: int, endTime: int) -> bool:
        if all( e1 <= startTime or endTime <= s1 for s1,e1 in self.segs): # no overlap
            self.segs.append([startTime, endTime])
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
