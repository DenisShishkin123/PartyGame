


class Cls:

    def __init__(self, a, b=1):
        self.a = a
        self.b = b


    def __del__(self):
        print("deleted")





# c = Cls(0)
# print(c.__dict__)
# print("*")
# # c = 1
# print("*")


# venv/Scripts/activate.bat
# venv\Scripts\activate.bat



def longest(a1, a2):

    return "".join(sorted(list(set([x for x in (a1+a2)]))))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
p = longest(a, b)

print(p)

# print([x for x in (a1+a2)])





# ///////////////////////////////////////////////////////


def decorator(fun):
    def f():
        print("********* start")
        fun()
        print("********* end")
    return f

def decorator2(fun):
    def f(*args, **kwargs):
        print("********* start")
        fun(*args, **kwargs)
        print("********* end")
    return f

@decorator2
def fun(*args):
    print("*")
    print(*args)

# p()
# p(1,2,3)

def decorator3(a):
    def decorator2(fun):
        def f(*args, **kwargs):
            print(a)
            print("********* start")
            fun(*args, **kwargs)
            print("********* end")
        return f
    return decorator2

# fun = decorator(fun)
# fun = decorator2(fun)
# fun = decorator3(fun, arg)
# @decorator
@decorator3("aaa")
def fun(*args):
    print("*")
    print(*args)

# p()
# p(1,2,3)










