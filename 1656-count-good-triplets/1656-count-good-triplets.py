class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans = 0
        n = len(arr)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    val1 = abs(arr[i]-arr[j])
                    val2 = abs(arr[j]-arr[k])
                    val3 = abs(arr[i]-arr[k])
                    if val1 <= a and val2 <= b and val3 <=c:
                        ans += 1
        return ans
        