class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        i = -1
        while tickets[k] != 0:
            i += 1
            i %= len(tickets)
            if tickets[i] == 0:
                continue
            tickets[i] -= 1
            time += 1
        return time

