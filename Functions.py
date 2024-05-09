class Test:
    # shows instanace method
    x=5
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print(self.a,self.b)
    @staticmethod
    def f2(self):
        print("hello")

    #Class Method we have to pass and argument
    @classmethod
    def f3(cls):
        print(cls.x)   
    
t1=Test(10,20)
t1.show()
Test.f3()
Test.f2()