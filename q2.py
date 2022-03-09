def lastcall(func):
    res = {}
    def inner_func(*args, **kwargs):
        key_res = str(args)
        if func.__name__ not in res.keys():  
            val = func(*args, **kwargs)
            res[func.__name__] = {key_res: val} 
        elif key_res in res[func.__name__]:
            val =f"I already told you that the answer is: {res[func.__name__][key_res]}!"
        else: 
            val = func(*args, **kwargs)
            res[func.__name__] = {key_res: val} 
        print(val)                   
    return inner_func

@lastcall
def f(x: int):
    return x ** 2
@lastcall
def f2(x: int):
    return x * 2

f(2)
f(2)
f(2)
f(3)
f(3)
f2(2)
f2(2)
f2(5)
f2(5)
f2(5)

