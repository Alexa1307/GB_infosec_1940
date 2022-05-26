'''
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
'''
#Вариант 1
my_list = [False, None, 301, 'True', True, 9.5, -13]
def get_type(el):
    for a in range(len(el)):
        print(type(el[a]))
get_type(my_list)

# Вариант 2
my_list = [False, None, 301, 'True', True, 9.5, -13]
for i in range(len(my_list)):
    print(type(my_list[i]))