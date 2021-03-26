def f1(func):
    def wrapper(*args,**kwargs):
        print('f1 started')
        a=func(*args,**kwargs)
        print('f1 ended')
        return a
    return wrapper
def f3(func):
    def wrapper(*args,**kwargs):
        print('f3 started')
        a=func(*args,**kwargs)
        print('f3 ended')
        return a
    return wrapper

@f1
def f(a,b):
    print(a+b)
a,b=map(int,input('enter the value: ').split())
f(a,b)

@f3
def f2(a,b):
    if(a+b)%2==0:
        print(f'{a}+{b} is {a+b} even')
    else:
        print(f'{a}+{b} is {a+b} odd')    
f2(a,b)   # x=f1(f)
          # x(a,b)
    
    