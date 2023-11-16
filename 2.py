x_0 = 1
x_1 = 1
s = 0
while x_1 < 4e6:
    if(x_1 % 2 == 0):
        s += x_1
    tmp = x_0
    x_0 = x_1
    x_1 = tmp + x_1
print(s)
