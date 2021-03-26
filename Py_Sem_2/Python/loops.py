# x=10;
# while x>0:
#     x = x//2;
#     print(x)


# Iterators
c = [5, 10, 15, 20]

#ArrayIndexOutofBounds
itr = iter(c)
while True:
    try:
        x = itr.__next__()
        print(x)
    except StopIteration: break


# iterator for dictionary
d = {'a':5,'b':105,'c':15,'d':20}

keys = d.keys()
values = d.values()
itr = iter(values)
big = 0
while True:
    try:
        value = itr.__next__()
        if(value>big):
            big = value
    except StopIteration:
        break
print(f'Biggest value is {big}')
