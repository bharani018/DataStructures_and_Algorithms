# MULTI LEVEL INHERITANCE

class Alpha:
    def __init__(self, lengt):
        self.lengt = lengt

class Beta(Alpha):
    def __init__(self, witdh, lengt):
        self.witdh = witdh

        Alpha.__init__(self, lengt)

    def Area(self):
        return self.lengt * self.witdh


class Gamma(Beta):
    def __init__(self, lengt, witdh, num):
        self.num = num
        Beta.__init__(self, witdh, lengt)

    def calculate(self):
        return self.lengt * self.num * self.witdh

    def cal2(self):
        return self.Area() * self.num

obj = Gamma(2,3,4)
print(obj.lengt)
print(obj.cal2())