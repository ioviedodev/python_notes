from datetime import datetime

def get_processor_time(func):
    def wrapper(*args,**kwargs):
        print("Into wrapper: ")
        initial_time=datetime.now()        
        func(*args,**kwargs)
        end_time=datetime.now()
        elapsed_time=end_time-initial_time
        print("elapsed_time: ",elapsed_time.total_seconds())
    return wrapper

@get_processor_time
def sum(*args,**kwargs):
    total=0
    for item in args:
        total+=item
    for item in kwargs.values():
        total+=int(item)        
    print("suma: ",total)
    return total   

@get_processor_time
def sum_first_n(n):
    total=0
    for item in range(n):
        total+=item
    print("suma: ",total)
    return total   

def run():
    a=10
    sum(a,5,4,3,2,1, b=10)
    sum_first_n(5000000)
    
if __name__=='__main__':
    run()