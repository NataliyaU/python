n = int(input('Введите число '))

if n < 0:
    print('Необходимо было ввести целое положительное число')
else:
    i = n % 10

    while n >= 1:
        n = n // 10
        if i < (n % 10):
            i = n % 10
    print('Самая большая цифра в числе:', i)