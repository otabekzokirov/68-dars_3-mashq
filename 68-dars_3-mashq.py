son=int(input('son:'))
a=len(str(son))
b=int(a)
for i in range(1,b+1):
    c=int(son)%10
    son=son//10
    print(c,end=(''))
