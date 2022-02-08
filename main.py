#random.uniform(start, stop)

# очень важно

# str.replace(шаблон, замена[max count], optional)  optional argument - количество замен

    # s = 'Hello world!'
    # result = s.replace('l', 'd', 1)

# print(result)

# str.split(symbol)

# s = 'hello world'
# result = s.split()
# print(result)

# # s.isdigit() проверяет строку на наличие только цифр
# s = '125'
# print(s.isdigit())

# s.isalpha() состоит ли только из букв
#пробел - это не буква, а символ

# s = "hello world"
# print(s.isalpha())

# s.isalnum() состоит ли из цифр или букв
# s = "Helloworld55"
# print(s.isalnum())

# s.islower() проверка нижнего регистра
# s.isupper() проверка верхнего регистра

# s.isspace() проверка на неотображаемые символы " " \n \t
# s = ' '
# print(s.isspace())

# s.istitle() проверка начинаются ли слова с заглавной буквы. Каждое
# слово должно начинаться с большой буквы
# s = 'hello'
# print(s.istitle())

# s.upper() - все символы становятся в верхнем регистре
# s.lower() - все символы в нижнем регистре

# s.title() - первая верхний, остальное - нижний
# s = 'hElLo wOrLd!'
# print(s.title())

# s.startswith(str) - начинается ли строка с шаблона
# s = "Hello world"
# print(s.startswith('H'))

# s.endswith() - заканчивается ли строка с шаблона

# s.capitalize() ТОЛЬКО первый символ в верхний, а остальное в нижний
# s = 'nJnbKvCdC'
# print(s.capitalize())

# title() - приводит каждое слово к Верхнему регистру

# s = "hello"           ###### ОЧЕНЬ ВАЖНО!!!!!!
# print('e' in s)       ###### Проверка на содержание

# s.swapcase() переводит верхний регистр в нижний и наоборот

s = 'Hello World'

# print(s.swapcase())

# count(str, [start], [end])  ### подсчет шаблона в строке (строка ограничивается аргументами)
# print(s.count('l'))

# .lstrip([chars]) удаление пробельных символов в начале строки l-eft
# .rstrip([chars]) удаление пробельных символов в конце строки R-ight
# .strip([chars]) удаление пробельных символов вообще

# множественная печать ALT
# ctrl f5

# .zfill(width) - строка не меньше длины width, в противном случае заполнит нулями
# s = input("enter: ")
# print(s.zfill(15))


# email = input('Enter your email: ')


# if email.endswith('@gmail.com') or email.endswith('@email.com'):
#     password = input('Enter your password: ')
#     password_confirmation = input('Enter password again: ')
#     if password == password_confirmation:
#         print("Registration is successful!")
#     else:
#         print("Passwords aren't the same")
# else:
#     print("Email should end with email.com or gmail.com")

# print("\a")



line = "The quick brown fox jumps over the lazy dog"
print(id(line))

line = line.replace('o', '*')

print(line)
print(id(line))