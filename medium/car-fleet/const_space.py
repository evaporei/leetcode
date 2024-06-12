class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted((pos, spd) for pos, spd in zip(position, speed))
        fleets = curr_time = 0
        for pos, spd in reversed(pairs):
            dest_time = (target - pos) / spd
            if curr_time < dest_time:
                fleets += 1
                curr_time = dest_time
        return fleets
