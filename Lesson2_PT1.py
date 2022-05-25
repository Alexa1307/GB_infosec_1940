'''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
'''
#Вариант 1
list =[False, None, 301, 'True', True, 9.5, -13]
def type1(el):
    for el in range(len(list)):
        print(type(list[el]))
    return
type1(list)

# Вариант 2
my_list = [False, None, 301, 'True', True, 9.5, -13]
my_list_len = len(my_list)
for i in range(0, my_list_len):
    print(type(my_list[i]))