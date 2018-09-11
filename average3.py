def main():
    work=add_three(1,1,10)
    ans= divide_three(work)
    print('This is the output of divide_three:{}'.format(ans))

def add_three(v1, v2, v3):
    """Adds three numbers together
    :param v1: number one
    :param v2: number two
    :param v3: number three"""
    a= v1 + v2 + v3
    print(a)
    return a


def divide_three(input):
    """Divides input by 3"""
    soln=input/3
    print(soln)
    return soln

if __name__== "__main__":
    main()    
    
