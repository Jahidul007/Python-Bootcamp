def jobScheduling( startTime, endTime, profit) -> int:
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

    dp = [p for i, j, p in jobs]

    for i in range(1, len(jobs)):
        dp[i] = max(dp[i], 0 if i == 0 else dp[i - 1])
        for j in range(i - 1, -1, -1):
            if jobs[j][1] <= jobs[i][0]:
                dp[i] = max(dp[i], dp[j] + jobs[i][2])
                break

    return dp[-1]-1

if __name__ == '__main__':
    test = int(input())
    startTime = []
    endTime = []
    profit = []
    startTime = list(map(int, input().split()))[:test]
    endTime = list(map(int, input().split()))[:test]
    profit = list(map(int, input().split()))[:test]


    print(str(jobScheduling(startTime,endTime, profit)))
