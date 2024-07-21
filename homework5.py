immutable_var_1 = 1, 3, 5, True, 'apple'
print('Immutable tuple, вариант 1:', immutable_var_1)
immutable_var_2 = (1, 3, 5, True, 'apple')
print('Immutable tuple, вариант 2:', immutable_var_2)
immutable_var_3 = tuple([1, 3, 5, True, 'apple'])
print('Immutable tuple, вариант 3:', immutable_var_3)
immutable_var_3 = (1, 3, 5, True, 'peach') # замена и способа определения кортежа, и последнего элемента в нем
print('Immutable tuple, замена кортежа ЦЕЛИКОМ для изменения значения одного элемента:', immutable_var_3)
print(immutable_var_3[4]) # вывод одного элемента кортежа
# immutable_var_1[4] = peach # попытка изменения значения элемента в кортеже
# print(immutable_var_1[4]) # вывод одного - измененного - элемента: TypeError: 'tuple' object does not support item assignment
# Кортеж является неизменяемой коллекцией элементов, поэтому изменить значения элемента(ов) невозможно
mutable_var_1 = [1, 3, 5, True, 'apple']
print('Mutable list, вариант 1:', mutable_var_1)
mutable_var_2 = list([1, 3, 5, True, 'apple'])
print('Mutable list, вариант 2:', mutable_var_2)
mutable_var_1[4] = 'peach' # изменение значения одного элемента в списке и вывод этого элемента
print(mutable_var_1[4]) # изменение значения одного элемента в списке и вывод этого элемента
# Список - изменяемая коллекция элементов
print('Mutable list, измененный вариант списка:', mutable_var_1)