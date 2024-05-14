class Fourcal:
    def setdata(self,first,second): # 파이선만 처음에 self라고 들어감(굳이 self아니어도되는데 뭐가하나있긴해야됨)
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = Fourcal()

a.setdata(4,2)
print(a.first)
print(a.second)
print(a.add())
