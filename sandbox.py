def sobes():
    print(c)
    d = [[]]*3
    print(d)
    d[0]=10
    print(d)
    d[1].append(11)
    print(d)
a = [1,2,3,4]
def razvorot(a):
    b = a[::-1]
    print(b)

def razv_manual(a):
    b = []
    for i in range(len(a)-1, -1, -1):
        print(i)
        b.append(a[i])
    print(b)

b = [3,6,7,1]

def odin(a,b):
    count =0
    for i in a:
        for j in b:
            if j==i:
                print("Odin")
                count+=1
    print(count)

#razvorot(a)
#razv_manual(a)
#odin(a,b)
#print(9//10)
def ch():
    count=0
    x = 12456
    sum = 0
    while x>0:
         count +=1
         sum=sum+x%10
         #print(sum)
         x = x//10
    print(count)
    print(sum)
#ch()
print(17//10)
print(14/10)
print(14%10)
#print("It should be deketed")