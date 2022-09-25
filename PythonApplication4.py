import math
class Parent:
    def __init__(self, n):
        self.n = n
        self.sides = [0 for i in range(n)]
    def inputSides(self):
        self.sides = [int(input("Side "+str(i+1)+" : ")) for i in range(self.n)]
    def findArea(self):
        s = 0
        for x in self.sides:
            #print (x,"\n")
            s = s + x
        #print (s,"\n")
        s = s/2
        e = s
        for x in self.sides:
            e = e * (s-x)
            #print (e,"\n")
        area = math.sqrt(e)
        print('Area ', area)

class Triangle(Parent):
    def __init__(self):
        Parent.__init__(self,3)
    def findArea(self):
        Parent.findArea(self)
    
t = Triangle()
t.inputSides()
t.findArea()