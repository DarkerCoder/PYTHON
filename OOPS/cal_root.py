class cal:
    def __init__(self,n):
        self.n = n
    
    def square(self):
        print(f'The square of {self.n} is : {self.n*self.n}')

    def cube(self):
         print(f'The cube of {self.n} is : {self.n*self.n*self.n}')

    def sqrt(self):
        print(f'The squareroot of {self.n} is : {self.n**(1/2)}')

a = int(input('Enter the number: '))
c = cal(a)
c.square()
c.cube()
c.sqrt()