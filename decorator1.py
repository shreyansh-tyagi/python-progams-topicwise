def f1(func):
    def wrapper(*args,**kwargs):
        print('started')
        a=func(*args,**kwargs)
        print('ended')
        return a
    return wrapper

@f1
def f(a,b):
    print(a+b)
a,b=map(int,input('enter the value: ').split())
f(a,b)

@f1
def f2(a,b):
    if(a+b)%2==0:
        print(f'{a}+{b} is {a+b} even')
    else:
        print(f'{a}+{b} is {a+b} odd')    
f2(a,b)   # x=f1(f)
          # x(a,b)
    
    