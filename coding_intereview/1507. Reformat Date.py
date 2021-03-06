class Solution:
    def reformatDate(self, date: str) -> str:
        parts = date.split()
        
        day = int(parts[0][:-2])
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"].index(parts[1]) + 1
        year = int(parts[2])
        
        return '{:04d}-{:02d}-{:02d}'.format(year, month, day)
