def func1(text):
    a=text(int(input('enter the number: ')))
    return a
def func2(text):
    if text%2==0:
        print('even')
    else:
        print('odd')
func1(func2)
            