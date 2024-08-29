class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0

        # everyone till k
        # let's buy their tickets
        for i in range(k+1):
            time += min(tickets[i], tickets[k])

        # everyone after k
        for i in range(k+1, len(tickets)):
            time += min(tickets[i], tickets[k] - 1)

        return time
