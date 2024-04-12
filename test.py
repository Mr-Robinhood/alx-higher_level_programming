global_var = 10

def func():

    ans = 0

    for i in range (1000):

        ans+= global_var * i

        return ans
    
func()