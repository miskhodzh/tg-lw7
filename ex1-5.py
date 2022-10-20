# Проработать примеры из методички:

# 1.Деструктуризация
# 2.Кортежи, множественное присваивание и обмен значениями
# 3.Создание кортежа из итерированного объекта
# 4.Метод index(). Поиск позиции элемента в кортеже
# 5.Метод count(). Количество вхождений элемента в кортеж

print('1.Деструктуризация')
name_and_age = ('Bob', 42)
(name, age) = name_and_age
print(name, age)

print('2.Кортежи, множественное присваивание и обмен значениями')
(a, b, c) = (1, 2, 3)
print(a)
print(b)
print(c)

print('3.Создание кортежа из итерированного объекта')
d = tuple('Hello')

lst = [2, 'abc', 3.88]
print(lst)
e = tuple(lst)

print('4.Метод index(). Поиск позиции элемента в кортеже')
A = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")

day = input('Введите день недели >>> ')

if day in A:
    num = A.index(day)
    print('Номер дня недели -', num + 1)
else:
    print('Неверный формат ввода')
    print('Введите: ',"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")

print('5.Метод count(). Количество вхождений элемента в кортеж')
A = ("ab", "ac", "ab", "ab", "ca", "ad", "jklmn")

d1 = A.count('ab')
d2 = A.count('jprst')
d3 = A.count('ca')

print('d1 =', d1)
print('d2 =',d2)
print('d1 =',d3)