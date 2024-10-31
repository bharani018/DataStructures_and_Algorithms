#MULTIPLE INHERITANCE - WHEN A CLASS IS DERIVED FROM TWO OR MORE BASE CLASS IT IS KNOWN AS MULTIPLE INIHERITANCE


class Maths:

    def __init__(self, Mat_mark):
        self.Mat_mark = Mat_mark

class Physics:

    def __init__(self, phy_mark):
        self.phy_mark = phy_mark

class Chemistry:

    def __init__(self, Chem_mark):
        self.Chem_mark = Chem_mark

class Cutoff(Maths, Physics, Chemistry):

    def __init__(self, Mat_mark, phy_mark, Chem_mark):
        Maths.__init__(self, Mat_mark)
        Physics.__init__(self, phy_mark)
        Chemistry.__init__(self, Chem_mark)

    def CalculateCutoff(self):
        return self.Mat_mark + (0.5 * self.phy_mark) + (0.5 * self.Chem_mark)

myCutoff = Cutoff(90, 92, 94)
print(myCutoff.CalculateCutoff())