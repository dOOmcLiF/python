a = 5
def test():
    global a
    a = 7

test()
print(a)