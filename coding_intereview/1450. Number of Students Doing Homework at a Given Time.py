class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        working = 0
        for i, stu in enumerate(startTime):
            if stu <= queryTime and endTime[i] >= queryTime:
                working += 1

        return working