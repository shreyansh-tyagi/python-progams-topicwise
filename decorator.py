def fun(func):
    def wrapper():
        print('started')
        func()
        print('ended')
    return wrapper    
def f():
    print('hello')
x=fun(f)      
x()