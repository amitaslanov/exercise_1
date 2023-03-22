def my_func(x1,x2,x3):
    if isinstance(x1, int) or isinstance(x2, int) or isinstance(x3, int):
        print('Error: parameters should be float')
    elif isinstance(x1, str) or isinstance(x2, str) or isinstance(x3, str):
        print('None')
    elif x1+x2+x3==0:
        print('Not a number – denominator equals zer')
    else:
        result=((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
        print(result)
