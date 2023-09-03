# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!


def minimum(arr): 
    small_ = arr[0] 
    for j in arr:
        if j < small_:
            small_ = j  
    return(small_)   


def maximum(arr): 
    big_ = arr[0]
    for i in arr:
        if i > big_:
           big_ = i
    return big_   

list1 = [4,6,2,1,9,63,-134,566]
result = minimum(list1)
result1 = maximum(list1)
print('max = ', result1, ', ' 'min = ', result, sep = '')     # max = 566, min = -134

list1 = [-52, 56, 30, 29, -54, 0, -110]
result = minimum(list1)
result1 = maximum(list1)
print('min = ', result, ', ' 'max = ', result1, sep = '')     # min = -110, max = 56

list1 = [42, 54, 65, 87, 0]
result = minimum(list1)
result1 = maximum(list1)
print('min = ', result, ', ' 'max = ', result1, sep = '')     # min = 0, max = 87
    
list1 = [5]
result = minimum(list1)
result1 = maximum(list1)
print('min = ', result, ', ' 'max = ', result1, sep = '')     # min = 5, max = 5



