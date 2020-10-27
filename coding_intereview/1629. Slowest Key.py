import operator
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        length = len(keysPressed)
        slowest_key = [releaseTimes[0], keysPressed[0]]
        for k in range(1, length):
            duration = releaseTimes[k] - releaseTimes[k - 1]
            if duration >= slowest_key[0]:
                slowest_key = max(slowest_key, [duration, keysPressed[k]])
        return slowest_key[1]
        
