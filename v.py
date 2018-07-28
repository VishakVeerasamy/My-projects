a=[1,2,3,4,5]
z=0
b= []
count=1
flag =0
def fun(x):
    y=len(x)
    f=0
    for i in range(y-1):
        if((x[i]==(x[i+1]+1)%5 and y==2)):
                return 0
        elif(x[i]+1==x[i+1]):
                f+=1
                if((f==2)and(y<=3) or y==2):
                    return 0
    return 1

def fun1():
    global z
    if(z==0):
        for i in x:
            b.append(i)
        for i in x:
            a.remove(i)
            z=1
    elif(z==1):
        for i in x:
            a.append(i)
        for i in x:
            b.remove(i)
            z=0
    return

print("River Bank A:{0}\nRiver Bank B:{1}".format(a,b))
while count<=20:
    if(z==0):
        print('\nRaft in River Bank A')
    elif(z==1):
        print('\nRaft in River Bank B')
    x=list(eval(input("Enter the items to be transported:")))
    if(len(x)>2):
        print('The Raft can only hold two persons')
        print('count:%d'%count)
        count+=1
        continue
    for i in range(len(x)):
        if(z==0 and x[i] not in a):
             flag=0
             break
        elif(z==1 and x[i] not in b):
             flag=0
             break
        flag=1    
    if(flag==0):
        print('conflict')
        print('count:%d'%count)
        count+=1
        continue
    fun1()    
    if(len(a)==0):
        break
    c=[x,a,b]
    x.sort()
    a.sort()
    b.sort()
    y=list(map(fun,c))
    if(y[0]==0 or y[1]==0 or y[2]==0):
        fun1()
        print('conflict')
        print('count:%d'%count)
        count+=1
        continue
    print("River Bank A:{0}\nRiver Bank B:{1}".format(a,b))
    print('count:%d'%count)
    count+=1
if count<=20:
    print('win')
else:
    print('lose')
