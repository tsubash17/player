a=int(input())
s=int(input())
b=[]
for x in range(0,a):
    d=int(input())
    b.append(d)
b.sort()
if s in b:
    print("yes")
else:
    print ("no")
