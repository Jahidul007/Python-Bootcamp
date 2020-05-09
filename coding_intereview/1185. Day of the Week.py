import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        day_of_week_map = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        year -= month < 3
        return day_of_week_map[((year + int(year / 4) - int(year / 100) + int(year / 400) + t[month - 1] + day) % 7)]

