def div(a,b):
    print(a/b)
#decorators come to use when we want to alter the original function without touching it

def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

div1= smart_div(div)
div1(2,4)

