from itertools import  combinations
N=int(input())
val=input().split()
k=int(input())
count=0
t=0
for x in combinations("".join(val),k):
    if "a" in x:
        count+=1
    t+=1
print("{0:.3f}".format(count/t))



