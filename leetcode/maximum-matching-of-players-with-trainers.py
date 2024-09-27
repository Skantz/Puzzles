from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i = 0
        c = 0
        for j, e in enumerate(trainers):
            if len(players) - 1 < i:
                break
            if e < players[i]:
                continue
            else:
                c += 1
                i += 1
        return c
