class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def perimeter(self):
        return 2*(self.l+self.b)
    def area(self):
        return self.l*self.b
    def display(self):
        print("length=",self.l)
        print("width=",self.b)
        print("perimeter=",self.perimeter())
        print("area=",self.area())
