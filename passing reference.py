def fun1():
    print('called function')
def fun2(f):
    return f() #returning function
fun2(fun1)  #passing reference of the function 
# passing one function to another function