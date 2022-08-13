from itertools import count
import time

def fibo_gen(max=None):
    n1=0
    n2=1
    count=0
    max_count=max
    while True :
        if not max_count or count<max_count:
            if count==0:
                count+=1
                yield n1

            elif count==1:
                count+=1
                yield n2

            else:
                count+=1
                aux = n1+n2
                n1,n2=n2,aux
                yield aux
        else:
            break

if __name__=='__main__':
    fibonacci=fibo_gen(10)
    for element in fibonacci:
        print (element)
        time.sleep(1)                    