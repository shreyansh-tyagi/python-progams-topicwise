def fun1():
    print('called function')
def fun2(f):
    f() 
fun2(fun1)    