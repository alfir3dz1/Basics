n=[]
while True:
    x=input()
    if x=="+":
        a=n.pop()
        b=n.pop()
        c=a+b
        n.append(c)
    elif x=="-":
        a=n.pop()
        b=n.pop()
        c=a-b
        n.append(c)
    elif x=="*":
        a=n.pop()
        b=n.pop()
        c=a*b
        n.append(c)
    elif x=="/":
        a=n.pop()
        b=n.pop()
        c=a/b
        n.append(c)
    else:
        g=int(x)
        n.append(g)
    print(n)
