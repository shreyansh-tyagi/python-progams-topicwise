def fun(func): #reference of f function will come to func variable
    def wrapper(): 
        print('started')
        func() #calling the f function because func contain the reference of f function therefore the control will move to the reference of f function and execute that block first
        print('ended') #control come back to this statement and start executing the from here
    return wrapper   #returning the wrapper function and calling the wrapper function 
def f():
    print('hello')
x=fun(f)  #calling function fun and passing the reference of f function    
x() #calling function 