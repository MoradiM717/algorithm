class Solution:

    def solve(self):
        name, weights = self.read()
        return self.solution(name, weights)

    def read(self) -> tuple[str, list[int]]:
        input()
        line = input()
        weights = list(map(int, line.split(" ")))
        name = input()
        return (name, weights)
    
    
    @staticmethod
    def _create_teams(weights: list[int]):
        ali: list[int] = []
        romina: list[int] = []
        if not weights:
            return ali, romina
        sorted_weights = sorted(weights, reverse=True)
        romina.append(sorted_weights[0])
        idx = 1
        alis_turn = True
        picked_one = False
        while idx < len(sorted_weights):
            if alis_turn:
                if picked_one:
                    alis_turn = False
                    picked_one = False
                else:
                    picked_one = True
                ali.append(sorted_weights[idx])
            else:
                if picked_one:
                    picked_one = False
                    alis_turn = True
                else:
                    picked_one = True
                romina.append(sorted_weights[idx])
            idx += 1
        return romina, ali      

    def solution(self, name: str, weights: list[int]) -> tuple[int, list[str]]:
        romina, ali = self._create_teams(weights)
        sum_ali = sum(ali)
        sum_romina = sum(romina)
        picked: list[str] = []
        picked_sum = 0
        idx = 0
        if name == "romina":
            if sum_romina > sum_ali:
                return idx, picked
            while idx < len(ali) and sum_romina <= sum_ali - picked_sum:
                picked.append(str(ali[idx]))
                picked_sum += ali[idx]
                idx += 1
            return (idx, picked)
        else:
            if sum_ali > sum_romina:
                return idx, picked
            while idx < len(romina) and sum_ali <= sum_romina - picked_sum:
                picked.append(str(romina[idx]))
                picked_sum += romina[idx]
                idx += 1
            return (idx, picked)



s = Solution().solve()
print(s[0])
if s[1]:
    print(" ".join(s[1]))
