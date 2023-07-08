class num:
    def __init__(self,p):
        self.p=p

    def con(self):
        z=[]
        for i in self.p:
            if i in self.p:
                if i not in z:
                    z.append(i)
        print(z)
        for j in z:
            count=0
            for i in self.p:
                if i==j:
                    count=count+1
            print(count,j)

v=num(p=[1,1,1,1,3,3,3,3,4,4,4,4])
v.con()
x=[5,10,15,15,10]
k=[]
[k.append(i) for i in x if i not in k] #list comprehension
print(k)

x=['1','2','3','4']
k=[int(i) for i in x ]
print(k)


x=[1,2,3,4,5]
f=[i*i for i in x if i%2==0]
print(f)
p=['hello','my','new','nothing']
j=[i for i in p  if len(i)>2]
print(j)
p=['hey','new','hyderabad']
v=[i.upper() for i in p]
print(v)
y='he1231189n12ew'
s=[i for i in y if i.isnumeric()]

print(s)
a=['1',5,'9',100,'0']
c=[i for i in a if type(i)==int]
print(c)

def f1(function):
    print(function(20,40))

def f2(p,q):
    return p+q
f1(f2)

def sum1(x,y):
    return x+y
def square(function):
    a=function(10,20)
    b=a**2
    print(b)
square(sum1)

def sub1(x,y):
    return x-y
def square(function):
    a=function(20,10)
    b=a**2
    print(b)
square(sub1)

def myunique(x):
    z=[]
    for i in x:
        if i not in z:
            z.append(i)
    return(z)
def mysum(function):
    sum=0
    a=function(x=[1,1,1,1,12,2,2,4,4,4,4,6,6,6,6])
    for i in a:
        sum=sum+i
    print(sum)
mysum(myunique)





    