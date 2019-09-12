
def sobes():
    #print(c)
    d = [[]] * 3
    print(d)
    d[0] = 10
    print(d)
    d[1].append(11)
    print(d)

a = [1, 2, 3, 4]

def razvorot(a):
    b = a[::-1]
    print(b)

def razv_manual(a):
    b = []
    for i in range(len(a) - 1, -1, -1):
        print(i)
        b.append(a[i])
        print(b)

#b = [3, 6, 7, 1,4]

def odin(a, b):
    count = 0
    for i in a:
        for j in b:
            if j == i:
                print("Odin")
                count += 1
    print(count)

    # razvorot(a)
    # razv_manual(a)
    # odin(a,b)
    # print(9//10)
def ch():
    count = 0
    x = 12456
    sum = 0
    while x > 0:
        count += 1
        sum = sum + x % 10
            # print(sum)
        x = x // 10
    print(count)
    print(sum)

    # ch()
#print(17 // 10)
#print(14 / 10)
#print(1 % 10)
#print("It should be deketed")

def fizz():
    for i in range(1, 101, 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FIZZ BUZZ")
        if i % 3 == 0:
            print("FIZZ")
        if i % 5 == 0:
            print("BUZZ")
        else:
            print(i)

    # fizz()
    s = "inna"
    v = "inna"
    # if s==v:
    #    print("Equla")
    print(s + v)
    print(1 + s)


#test_met()

from  mimesis import Person
def persin_test():
    person = Person("en")
    print("u")
    user_info = dict(username=person.username(), email=person.email(),password=person.password(),
                     real_name=person.full_name(), gender='men', birthday = ("1","3","1990"))
    print(user_info)

def vstavka():
    lst = [1,3,5]
    lst_2 = [2,4]
    j=1
    for i in lst:
        lst_2.insert(j,i)
        j+=2
    print(lst_2)
#x = (i for i in range(1,10))
#print(x.__next__())
#print(x.__next__())
#print(x.__next__())
import random
print(int(random.random()*100))
#a =[1,2,3,4]
#b = [i+5 for i in a]
#print(b)
#print(b[1])
#c = list(map(a,b))
#print(c)
#print(c.__next__())
b = ["d","a","b","c","6"]
print(id(b))
b.append("r")
print(id(b))
z={"x":"e",1:45,"er":3}
#def um(v):
#    return v*v
#c = list(map(um,a))
#for i in c:
#    print(i)
print(z.keys())
print(sorted(b))
if "e" in z:
    print(("yes"))
print(z.get('f',1))
w=(3,6)
print(id(w))
w=w+(4,5)

print(id(w))
class Worker:
    def __init__(self, name, pay): # Инициализация при создании
        self.name = name # self – это сам объект
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1] # Разбить строку по символам пробела
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

wor = Worker("inna korsun",12)
print(wor.lastName())
x=3
print(repr(w))
