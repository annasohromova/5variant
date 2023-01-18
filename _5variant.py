


#1 Напишите программу, которая по данному числу n от 1 до 9 выводит на экран n домов. 
#Между двумя соседними домами также имеется пустой (из пробелов) столбец. 
#Разрешается вывести пустой столбец после последнего дома. Для упрощения рисования скопируйте дом из примера в среду разработки.


#dom = ['  ~~~~~  ',
#       ' /_____\\ ',
#       ' | []  | ',
#       '  -----  ']
#n = 6
#for i in dom:
#    print(i * n)





#2 Известны оценки по физике каждого ученика двух классов. Определить среднюю оценку в каждом классе. Количество учащихся в каждом классе одинаковое.



#n=int(input("sisestage õpilaste arv ->"))
#if n>2:
#    print("1", end=" ")
#    a=1
#    b=0
#    for i in range(2, n+1):
#        a, b=b, a+b
#        a=b
#        b=a+b 
#        print(b, end="")
#else:
#    print("Arv ei tohi olla väiksem kui kolm")
#    print()



#3 Известны средние оценки каждого из  учеников класса. Определить минимальную и максимальную оценки. 
#(Оценки и количество учеников получаем случайным образом). 
#Использовать только цикл и сравнительные операторы. max() и min() не использвать.


from math import*
from random import*


num_students = 10 
min_grade = 100 
max_grade = 0 

for i in range(num_students):
    grade = randint(0, 100) 
    if grade < min_grade:
        min_grade = grade
    if grade > max_grade:
        max_grade = grade

print("Minimum grade:", min_grade)
print("Maximum grade:", max_grade)




#ДОДЕЛЫВАЮ ДОМА