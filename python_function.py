def func1():
    print('i am inside the function')
def func2(num):
    if(num>0):
        print(f'{num} is greater than zero')
    else:
        print(f'{num} is less than zero')
fun3=func2       
func_var=func1
print(func_var())
num=int(input('enter the number: '))
print(fun3(num))           
def retfun(func1):
    print(func1)   
retfun(func1) 
 