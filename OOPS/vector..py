class twDVector:
    def __init__(self,i,j):
        self.i = i
        self.j =j
    
    def show(self):
        print(f'3D vector --> {self.i}i + {self.j}j')
        
class threeDVector(twDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j) # type: ignore
        self.k = k
    
    def show(self):
        print(f'3D vector --> {self.i}i + {self.j}j + {self.k}k')

tv = twDVector(4,5)
tv.show()

thv = threeDVector(2,3,4)
thv.show()