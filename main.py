# 46
class DivBy3:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return [i for i in range(self.n) if i % 3 == 0]

print(DivBy3(int(input())).solve())

# 47
class DivBy5:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return [i for i in range(self.n) if i % 5 == 0]

print(DivBy5(int(input())).solve())

# 48
class DivBy3and5:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return [i for i in range(self.n) if i % 3 == 0 and i % 5 == 0]

print(DivBy3and5(int(input())).solve())

# 49
class SumDiv3:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return sum(i for i in range(self.n) if i % 3 == 0)

print(SumDiv3(int(input())).solve())

# 50
class SumDiv5:
    def __init__(self, n):
        self.n = n
    def solve(self):
        return sum(i for i in range(self.n) if i % 5 == 0)

print(SumDiv5(int(input())).solve())
