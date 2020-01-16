#Подсчитать частоту повторов каждого уникального слова в файле:
def count_word(filename):
    import string
    import sys
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"+ ","
    for line in open(filename):
        for word in line.lower().split():
            print(word)
            word = word.strip(strip)
            print(word)
            if len(word) >= 1:
               words[word] = words.get(word, 0) + 1
    for word in sorted(words):
        print("'{0}' occurs {1} times".format(word, words[word]))
#count_word("text.txt")
#ряд фибоначчи - найти 10 член
def fibonacci(n):
    rd = []
    for i in range(0,n):
        if i==0:
            rd.append(1)
        if i==1:
            rd.append(1)
        if i>1:
            rd.append(rd[i-1]+rd[i-2])
    print(rd[-1])
#fibonacci(5)
def fibonacci2(n):
    rd = [1,1]
    for i in range(2,n):
        rd.append(rd[i-1]+rd[i-2])
        print(rd[i])
    print(rd[-1])
#fibonacci2(7)
#сериализация файлов
def work_with_file(filename):
    dt = {1:34,3:'56'}
    with open(filename,'wb') as work_file:
        import pickle
        pickle.dump(dt,work_file)
#work_with_file("text.txt")
#десериализация файлов
def work_with_file2(filename):
    with open(filename,'rb') as work_file:
        import pickle
        print(pickle.load(work_file))
#work_with_file2("text.txt")
#import pathlib
#print(pathlib.Path('./text.txt').is_file())

def decorator_f(inna):
    print("Hello from decorator")
    inna()
    print("By!")

#@decorator_f(iters=2)
#def inna():
#    print("Hello from function inna")

def str_insrt(f):
    new_str=''
    for i in range(0,len(f),2):
        new_str=new_str+f[i:i+2]+"-"
    #new_str=new_str.rstrip("-")
    #print(new_str,file=open('text.txt','a'))
    print(new_str)

#str_insrt("farada")

def tst_r():
    d = lambda x:x+1
    print(d(2))
    x=1
    tests={2:3,4:5,6:7}
    items={2,6,9,2}
    s=set(items)
    print(s)
    for key in tests: # Для всех ключей
        if key in items: # Позволить интерпретатору отыскать совпадение
            print(key, 'was_found')
        else:
            print(key, 'not found!')
#res=2
def inna():
    global res
    res=1
    return res
s = {True:0, False:1, 1:'spam'}
#print(s)
def file_tst(file_name):
    c = 0
    with open(file_name) as file_t:
        for line in file_t:
            for i in line:
                if i.isupper():
                    c = c+1
    print(c)
#file_tst("text.txt")

def file_tst2(file_name):
    with open(file_name) as file_t:
        s = [i for line in file_t for i in line if i.isupper()]

        with open ('text2.txt', 'w') as file_w:
            file_w.write(str(len(s)))

file_tst2("text.txt")
def t_2():
    d=["i","n","n"]

    print(s)
t_2()
