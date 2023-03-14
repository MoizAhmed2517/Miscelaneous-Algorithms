import time

for k in range(1,10):
    a=time.time()
    print(a)

B=list(range(100000,0,-1))

def mergesort(A):
    n=len(A)
    s=list()
    if n==1:
        s=A
    else:
        a=(n//2)
        s1=mergesort(A[0:a])
        s2=mergesort(A[a:n])
        s=merge(s1,s2) 
    return s

def merge(A,B):
    n1=len(A)
    n2=len(B)
    A=A+[float('inf')]
    B=B+[float('inf')]
    i=j=0
    l=list()
    for k in list(range(n1+n2)):
        if A[i]<=B[j]:
            l=l+[A[i]]
            i+=1
        else:
            l=l+[B[j]]
            j+=1
    return l

print(mergesort(B))

# making A list
l=list()
for i in range(1,10):
    b=time.time()
    print(b)
    c=b-a
    l=l+[c]

print(l)
#taking an average of time:
sum=0
for m in range(0,len(l)):
    sum=sum+l[m]

total=len(l)
AveargeWorstCase=sum/total
print(round(AveargeWorstCase,8))