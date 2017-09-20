x=6
y=1
while(0<=x):print(" "*x,"*"*y);x=x-1;y=y+2


size = 9
q=1

while(0<=size):print(' '*size, '*'*q);size=size-1;q=q+1
print()

n = 8

for idx in range(n-1):
    print((n-idx) * ' ' + (2*idx+1) * '*')
for idx in range(n-1, -1, -1):
    print((n-idx) * ' ' + (2*idx+1) * '*')

