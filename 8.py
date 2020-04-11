import time
import psutil
import os

def calc_time(f):
    def wrapper(*args, **kwargs):
        t_start=time.time()
        f(*args, **kwargs)
        t_end=time.time()
        print(' Время выполнения: ',t_end-t_start)
    return wrapper

def calc_mem(f):
    def wrapper(*args, **kwargs):
        proc1=psutil.Process(os.getpid())
        mem_start=proc1.memory_info().rss/1000000
        f(*args, **kwargs)
        proc2=psutil.Process(os.getpid())
        mem_end=proc2.memory_info().rss/1000000
        print(' Занимаемый объем памяти: ',mem_end-mem_start)
    return wrapper

@calc_time
def my_div(*args, **kwargs):
    n=args[0]
    kdiv=args[1]
    ls=[]
    for i in range(n):
        ls.append(i/kdiv)

@calc_mem
def my_div3(*args, **kwargs):
    n=args[0]
    kdiv=args[1]
    ls=[]
    for i in range(n):
        ls.append(i/kdiv)

def my_div_gen(*args, **kwargs):
    n=args[0]
    kdiv=args[1]
    for i in range(n):
        yield i/kdiv


if __name__=="__main__":
# 1:
    my_div(1000, 10)
    my_div(10000, 10)
    my_div(100000, 10)
# 2:
    print("====== 2 =========")
    my_div(100000, 10)

    t_start2=time.time()
    mydivgen= my_div_gen(100000, 10)
    x= next(mydivgen)
    t_end2=time.time()
    print(' Время выполнения2: ',t_end2-t_start2,"  ",x)

    t_start2=time.time()
    x= next(mydivgen)
    t_end2=time.time()
    print(' Время выполнения2: ',t_end2-t_start2,"  ",x)

# 3:
    print("====== 3 =========")
    my_div3(100000, 10)

# 4:
    print("====== 4 =========")
    my_div3(1000000, 10)

    proc41=psutil.Process(os.getpid())
    mem_start4=proc41.memory_info().rss/1000000
    mydivgen= my_div_gen(100000, 10)
    x= next(mydivgen)
    proc42=psutil.Process(os.getpid())
    mem_end4=proc42.memory_info().rss/1000000
    print(' Занимаемый объем памяти: ',mem_end4-mem_start4)

    i=1
