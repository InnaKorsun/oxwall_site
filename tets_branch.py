from value_models.user import User

a = [1, 2, 3, 4]
b = [5, 6, 7]


def argses(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)


# argses(1,2,3,4)
# argses(5,6)

def kw(**kwargs):
    for i, j in kwargs.items():
        print(i, j)


# kw(q=34,e=45)

drinks = ["coffee", "tea", "milk", "water"]
for drink in enumerate(drinks):
    print(drink)


def tr(*kwargs):
    us = User(*kwargs)
    print(us.username)
    print(us.password)
    print(us.email)


tr('inna','solo')
