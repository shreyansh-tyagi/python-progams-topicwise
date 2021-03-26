def fun(func): #reference of f function will come to func variable
    def wrapper(*args,**kwargs): 
        print('started')
        func(*args,**kwargs) #calling the f function because func contain the reference of f function therefore the control will move to the reference of f function and execute that block first
        print('ended') #control come back to this statement and start executing the from here
    return wrapper   #returning the wrapper function and calling the wrapper function 
@fun #decorator
def f(a,b=10,c='shrey'):
    print(a,b,c)
f('hello')
#x=fun(f) #this line work as the decorator #calling function fun and passing the reference of f function    
#x() #calling function 
#instead of doing this we can use the way how to actually declare the decorator
#when a argument is passed inside the last function like in this case f function have one argument that is hello but the decorator 
#function doesn't have any argument the wrapper and the reference function func doesn't have any argument
#therefore pass *args and **kwargs to both of these function which allow us to give as many as argument you want to passed