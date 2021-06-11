"""
https://leetcode.com/problems/my-calendar-i/
"""


class MyCalendar:

    def __init__(self):
        self.starts = []
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        can_be_booked = True
        for booking in self.bookings:
            if booking[0] <= end < booking[1] or booking[0] <= start < booking[1]:
                can_be_booked = False
                break
            elif start < booking[0] < end or start < booking[1] < end:
                can_be_booked = False
                break
        if can_be_booked:
            self.bookings.append([start, end])
        return can_be_booked


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
