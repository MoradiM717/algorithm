class Solution:

    def solve(self):
        test_cases = self.read()
        for tc in test_cases:
            print(self.solution(case=tc))

    def read(self) -> list[int]:
        n = int(input())
        test_cases = []
        for _ in range(n):
            m = int(input().split(" ")[1])
            line = input(" ")
            test_cases.append((m, [int(i) for i in line.split(" ")]))
        return test_cases

    def solution(self, case: tuple[int, list[int]]):
        mapper = {}
        m = case[0]
        for item in case[1]:
            mod_res = item % m
            mapper[mod_res] = mapper.get(mod_res, 0) + 1
            
        counter = 1 if mapper.pop(0, 0) != 0 else 0
        
        for mod in range(1, (m // 2) + 1):
            motammam = m - mod

            if mod == motammam:
                if mapper.get(mod, 0) > 0:
                    counter += 1
            else:
                mod_value = mapper.get(mod, 0)
                motammam_value = mapper.get(motammam, 0)

                if mod_value > 0 or motammam_value > 0:
                    if abs(motammam_value - mod_value) <= 1:
                        counter += 1
                    else:
                        counter += 1 + (abs(motammam_value - mod_value) - 1)
                        
        return counter

s = Solution().solve()
