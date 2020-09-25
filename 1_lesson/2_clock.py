a = int(input('Введите секунды: '))

def digit(num):
    if (num / 10) < 1:
        num = '0' + str(num)
    return num

hour = digit(a // 3600)
min = digit(a % 3600 // 60)
sec = digit(a % 60)

print(f"{hour}:{min}:{sec}")