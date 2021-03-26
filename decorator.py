def fun(func): #reference of f function will come to func variable
    def wrapper(): 
        print('started')
        func() #calling the f function because func contain the reference of f function therefore the control will move to the reference of f function and execute that block first
        print('ended') #control come back to this statement and start executing the from here
    return wrapper   #returning the wrapper function and calling the wrapper function 
@fun #decorator
def f():
    print('hello')
f()
#x=fun(f) #this line work as the decorator #calling function fun and passing the reference of f function    
#x() #calling function 
#instead of doing this we can use the way how to actually declare the decorator