class Solution:        

    def solve(self):
        n, transactions = self.read()
        return self.solution(n, transactions)

    def read(self):
        n, m = map(int, input().split(" "))
        transactions: list[tuple[int, int, int]] = []
        for _ in range(m):
            transactions.append(tuple(map(int, input().split(" "))))
        
        return n, transactions
        

    def solution(self, n: int, transactions: list[tuple[int, int, int]]):
        overall: dict[int, int] = {}
        for transaction in transactions:
            _from = transaction[0]
            to = transaction[1]
            value = transaction[2]
            overall[_from] = overall.get(_from, 0) - value
            overall[to] = overall.get(to, 0) + value
        in_debts = []
        creditors = []
        for key, value in overall.items():
            if value > 0:
                creditors.append(key)
            elif value < 0:
                in_debts.append(key)
        creditors.sort(reverse=True, key=lambda x: overall[x])
        in_debts.sort(key=lambda x: overall[x])
        in_debpt_in_line = 0
        final_decisions = []
        for creditor in creditors:
            while overall[creditor] > 0:
                if overall[creditor] >= -overall[in_debts[in_debpt_in_line]]:
                    final_decisions.append((in_debts[in_debpt_in_line], creditor, -overall[in_debts[in_debpt_in_line]]))
                    overall[creditor] += overall[in_debts[in_debpt_in_line]]
                    in_debpt_in_line += 1
                else:
                    final_decisions.append((in_debts[in_debpt_in_line], creditor, overall[creditor]))
                    overall[in_debts[in_debpt_in_line]] += overall[creditor]
                    overall[creditor] = 0
        return final_decisions

s = Solution()
solution = s.solve()
print(len(solution))
for sol in solution:
    print(f"{sol[0]} {sol[1]} {sol[2]}")
