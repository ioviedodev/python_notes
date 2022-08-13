import time 
# FibonacciSeries using an Iterator

def validate_number():
    number=-1
    while True:
        number_str=input("Please input the n index to be print in the fibonacciSeries: ")
        if(number_str.isnumeric()):
            number=int(number_str)
            break
        else:
            print("Please input a valid number!!")
    return number  

class FiboIter():
    def __init__ (self,n_index=None):
        self.n_index=n_index

    def __iter__(self ):
        self.n1 = 0
        self.n2 = 1

        self.counter=0
        return self

    def __next__(self):
        if not self.n_index or self.counter<self.n_index:
            if self.counter == 0:
                self.counter+=1
                return self.n1
            elif self.counter == 1:
                self.counter+=1
                return self.n2
            else:
                self.aux = self.n1 + self.n2
                #swap
                # self.n1 = self.n2
                # self.n2 = self.aux
                #swap
                self.n1, self.n2 = self.n2 , self.aux
                self.counter+=1
                return self.aux
        else:
            raise StopIteration

if __name__=="__main__":
    number=validate_number()
    print("number: ",number)
    fibonacci = FiboIter(number)
    for element in fibonacci:
        print (element)
        time.sleep(0.05)