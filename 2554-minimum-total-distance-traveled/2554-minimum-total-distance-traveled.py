class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        
        n, m = len(robot), len(factory)
        dp = [[math.inf] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0  # Base case: no robots, no factories, no distance
        
        for i in range(1, n + 1):
            dp[i][0] = math.inf  # No factories to repair robots
        
        # Process factories and calculate min distance using DP
        for j in range(1, m + 1):
            position_j, limit_j = factory[j - 1]
            dp[0][j] = 0  # No robots to assign, zero distance
            
            # Try to assign k robots to factory j, with k <= limit of factory j
            for i in range(1, n + 1):
                dp[i][j] = dp[i][j - 1]  # Option to skip this factory
                
                total_distance = 0
                for k in range(1, min(i, limit_j) + 1):
                    total_distance += abs(robot[i - k] - position_j)
                    # Check minimum with k robots assigned to current factory
                    dp[i][j] = min(dp[i][j], dp[i - k][j - 1] + total_distance)
        
        return dp[n][m]
         