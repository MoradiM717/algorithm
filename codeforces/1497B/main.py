import sys
from collections import deque


class Node:
    def __init__(self, color) -> None:
        self.children = []
        self.color = color
        self.diff = 1 if color == "W" else -1
        self.is_leaf = True

    def __repr__(self) -> str:
        return f"{self.color} -- {self.diff} -- {self.is_leaf}"

    def insert_child(self, node: "Node"):
        self.children.append(node)
        self.is_leaf = False


class Solution:
    def solve(self):
        test_cases = self.read()
        for tc in test_cases:
            print(self.solution(root=tc))

    def convert(self, parents, colors):
        nodes: dict[int, Node] = {}
        root = Node(color=colors[0])
        nodes[1] = root
        for i in range(len(parents)):
            new_node = Node(color=colors[i + 1])
            nodes[parents[i]].insert_child(new_node)
            nodes[i + 2] = new_node
        return root

    def read(self):
        t = int(sys.stdin.readline())
        inputs = []
        for _ in range(t):
            sys.stdin.readline()
            line = sys.stdin.readline()
            parents = [int(v) for v in line.split(" ")]
            colors = sys.stdin.readline().strip()
            inputs.append(self.convert(parents, colors))
        return inputs

    def solution(self, root: Node):
        children = []
        stack = deque()
        stack.append(root)
        while stack:
            child: Node = stack.popleft()
            children.append(child)
            stack.extend(child.children)
        for i in range(len(children) - 1, -1, -1):
            if children[i].is_leaf:
                continue
            children[i].diff += sum((c.diff for c in children[i].children))
        return sum((1 for c in children if c.diff == 0))


s = Solution().solve()
