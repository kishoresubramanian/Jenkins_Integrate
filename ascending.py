a="6783451"
x,y=0,9
str=''
while y>=x:
    for i in a:
        if y==int(i):
            str=str+i
    y=y-1
print(str)
