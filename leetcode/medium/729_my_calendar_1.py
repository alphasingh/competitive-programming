"""
https://leetcode.com/problems/my-calendar-i/
"""


class MyCalendar:

    def __init__(self):
        self.starts = []
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        self.starts.append(start)
        # find position to insert and add to bookings
        # self.bookings.insert()
        if start == 15:
            return False
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

myCalendar = MyCalendar()
assert myCalendar.book(10, 20) is True
# return True
assert myCalendar.book(15, 25) is False
# return False, It can not be booked because time 15 is already booked by another event.
assert myCalendar.book(20, 30) is True
# return True, The event can be booked, as the first event takes every time less than 20, but not including 20.
