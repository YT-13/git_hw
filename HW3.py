#Завдання 1
# Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

# input_number = input('Введіть число: \n')
# input_word = input('Введіть слово:\n')
# if len(input_word) <= int(input_number):
#     print ('Введене слово має містити більше символів (мінімум на 1), аніж введене число!')
# else:
#     print ('The %s symbol in %s is \'%s\'' % (input_number, input_word, input_word[int(input_number)]))
#РОЗВЯЗОК:

while True:
    input_word = input('Введіть слово >>> ')
    if input_word:
        break
while True:
    input_number = input('Введіть число від 1 до %s >>> ' % len(input_word)).lstrip('0')
    if input_number.isdigit() and int(input_number) <= len(input_word):
        input_number = int(input_number)
        break

result_str = 'The %s symbol in %s is \'%s\'' % (input_number, input_word, input_word[int(input_number)-1])
print(result_str)

#Завдання 2
#Вести з консолі строку зі слів за допомогою input()
# (або скористайтеся константою). Напишіть код, який визначить кількість слів, в цих даних.
#РОЗВЯЗОК:

my_str = input('Вdедіть декілька слів через пробіл: \n')
result = my_str.split(' ')
print('Кількість слів = ' + str(len(result)))

#Завдання 3
# Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні (int, float), які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
#РОЗВЯЗОК:

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for index in lst1:
    if type(index) == int or type(index) == float:
        lst2.append(index)
print(lst2)



