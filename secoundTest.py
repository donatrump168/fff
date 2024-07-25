class Employee():
    def __init__(self, i, n, h , r):
        self.id=i;
        self.name=n;
        self.hour=h;
        self.rate=r;
    def toString(self):
        return str(self.id)+" "+self.name+"  "+str(self.hour)+" "+str(self.rate)+" ";

emp= Employee(1001, " Dona ", 100, 30);
print (emp.toString());