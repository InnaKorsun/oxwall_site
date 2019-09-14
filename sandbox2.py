#print(2.5.as_integer_ratio())
#Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].
#Выведите все элементы, которые меньше 5.
def zad_1():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in a:
        if i>5:
            print(i)
#zad_1()
#Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
def zad_2():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c =[]
    for i in a:
        for j in b:
            if i==j:
                c.append(j)
    print(c)
#zad_2()
#Отсортируйте словарь по значению в порядке возрастания и убыван
def zad_3():
    import operator
    dic = {2:34,3:56,1:456}
    a_keys = sorted(dic.items(),reverse=False)
    print(a_keys)

    b_values = sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
    print(b_values)
#zad_3()
#Напишите программу для слияния нескольких словарей в один.

def zad_4():
    my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    my_dict2 = {'g': 579, 'h': 5874,'a': 45}
    my = {}
    my = my_dict.copy()
    my.update(my_dict2.items())
    print(my)

#zad_4()
# Найдите три ключа с самыми высокими значениями в словаре my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}.
def zad_5():
    import operator
    my_dict = {'a': 500, 'b': 5878, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    lst=[]
    #c = sorted(my_dict.items(),key=operator.itemgetter(1))
    #print(c[-3:])
    #нахожу максимальные значения и в словаре ищу ключи
    for i in my_dict.values():
        lst.append(i)
    lst.sort()
    l=lst[3:]
    #print(l)
    #print(i)
    for j in l:
        for i in my_dict.items():
            if j==i[1]:
                print(i[0])

#zad_5()
#Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

#Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.
def zad_6():
    s = 5
    w =str(s)

#zad_6()

#Нужно вывести первые n строк треугольника Паскаля.
# В этом треугольнике на вершине и по бокам стоят единицы,
# а каждое число внутри равно сумме двух расположенных над ним чисел.
def zad_7():
    pascals_triangle = []

    def blank_list_gen(x):
        while len(pascals_triangle) < x:
            pascals_triangle.append([0])

    def pascals_tri_gen(rows):
        blank_list_gen(rows)
        for element in range(rows):
            count = 1
            while count < rows - element:
                pascals_triangle[count + element].append(0)
                count += 1
        for row in pascals_triangle:
            row.insert(0, 1)
            row.append(1)
        pascals_triangle.insert(0, [1, 1])
        pascals_triangle.insert(0, [1])

    pascals_tri_gen(6)

    for row in pascals_triangle:
        print(row)
#zad_7()
#Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
def zad_8():
    s = "hello"
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[-1 - i]:
            print("It's not palindrome")
    print("It's palindrome")

#zad_5()
#Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды.
def zad_9():
    count = int(input())
    print(count)
    day = count//86400
    hours = count//3600
    min = count // 60
    sec = count%60
    s = "{} + 'days', {} + 'hours' +{} + 'min' + {} +'sec'".format(day, hours,min ,sec)
    print(s)
#zad_9()
#Вы принимаете от пользователя последовательность чисел, разделённых запятой. Составьте список и кортеж с этими числами.
def zad_10():
    count = (input().split(","))
    count_list = []
    count_tuple = ()
    for i in count:
        i = int(i)
        count_list.append(i)
    count_tuple=tuple(count_list)
    print(count_list)
    print(tuple(count_tuple))
#zad_10()
#Выведите первый и последний элемент списка.
def zad_11():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(a[0],a[-1])
#zad_11()
#Напишите программу, которая принимает имя файла и выводит его расширение.
# Если расширение у файла определить невозможно, выбросите исключение.

def zad_12():
    import os
    s= "inna"
    s2="inna korsun"

    if s.find(s2):
        print("OK")
    else:
        print("Not exist")

    file_name = input("Enter ")   # file to be searched
    cur_dir = os.getcwd()  # Dir from where search starts can be replaced with any path
    print(cur_dir)
    file_list = os.listdir(cur_dir)
    print(file_list)


    for i in file_list:
        sr = i.split(".")
        print(sr[0])
        try:
            if file_name.index(sr[0]):
                print("File Exists in: ", cur_dir)
            else:
                print("Not exist")
        except ValueError:
            print("ok")
        break
#zad_12()
#При заданном целом числе n посчитайте n + nn + nnn.
def zad_13():
    n = int(input())
    n2=n+n*n+n*n*n
    print(n2)
#zad_13()
#Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.
def zad_14():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 237, 89, 66]
    for i in a:
        if i==237:
            break
        if i%2==0:
            print(i)

#zad_14()
#Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
def zad_15():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    for i in a:
        if i not in b:
            print(i)
#zad_15()
#Выведите список файлов в указанной директории.
def zad_16():
    import os
    dr = os.getcwd()
    print(os.listdir(dr))
#zad_16()
#Сложите цифры целого числа.
def zad_17():
    h  = 134000
    s=0
    for i in str(h):
        s+=int(i)
    print(s)
#zad_17()
#Посчитайте, сколько раз символ встречается в строке.
def zad_18():
    s = "rosott"
    d = {}
    for i in s:
        if i in d.keys():
            d[i] += 1
        else:
            d.update({i:1})
    print(d)
#zad_18()
#Поменяйте значения переменных местами.
def zad_19():
    a=3
    b=5
    b,a =a,b
    print(a,b)
#zad_19()
#С помощью анонимной функции извлеките из списка числа, делимые на 15.
def zad_20():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,30]
    b=[]
    for i in a:
        if i%15==0:
            b.append(i)
    print(b)
#zad_20()
#Нужно проверить, все ли числа в последовательности уникальны.#вывести уникальные
def zad_21():
    a = [1, 1, 2, 3, 4, 4]
    b=[]
    #setarr = set(a)
    #if len(a) == len(setarr):
    #    print("Все элементы уникальны")
    #else:
    #    print("Есть одинаковые")
    for i in range(len(a)+1):
        for j in range(i + 1, len(a)):
            if a[i] != a[j]:
                if a[j] not in b:
                    b.append(a[j])
    print(b)

#zad_21()
#Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное
def zad_22():
    st = "Напишите программу, которая которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное"
    from collections import Counter
    dic={}
    lst = st.split(" ")
    print(lst)
    for j in lst:
        if j in dic:
            dic[j] += 1
        else:
            dic[j]=1
     #второй способ найти наиболее встречающийся обьект
    #Counter = Counter(lst)
    #k = Counter.most_common(1)
    #print(k)
    max = 1
    for i in dic.values():
        if i>max:
            max=i
    print(max)
    for k in dic.items():
        if k[1]==max:
            print("Most common is "+str(k[0]))

    #Search largest word
    cou = {}
    for j in lst:
        if j in cou:
            pass
        else:
            cou[j]=len(j)
    print(cou)
    for i in cou.values():
        if i>max:
            max =i
    for i in cou.items():
        if i[1]==max:
            print("Most longer word is "+ str(i[0]))
#zad_22()
# Есть дав листа -  нужно соединить их   - первый елемент с первого листаб второй - со второго и т д
def zad_23():
    lst1=[1,3,5]
    lst2=[2,4,6,8,10]
    ind=1
    for i in lst2:
        lst1.insert(ind,i)
        ind=ind+2
    print(lst1)
#zad_23()
s="Inna"
s2='Inna'
print(s is s2)


print("Additional text for commit try 2 try 3 try4")
