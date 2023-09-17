# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
# Пример процедуры для сортировки списка чисел в порядке убывания, используя алгоритм сортировки выбором:

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)
numbers = [1, 2, 3, 4, 5]
sort = sort_list_declarative(numbers)
print(sort)   
# Вывод: [5, 4, 3, 2, 1]