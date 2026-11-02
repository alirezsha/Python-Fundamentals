def optional_number_arg(*args):
    for arg in args:
        print(arg)
        
def keyword_arg(**kwargs):
    for k, v in kwargs.items():
        print('%s == %s'%(k, v))

def average(a, *b):
    return (a + sum(b)) / (1 + len(b))
