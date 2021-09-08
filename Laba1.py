status = -1
spisok = []
sotr = []

while status != 2:
    print('Введите одну из следующих цифр для вызова одной из описанных команд:')
    print('0 - Открыть программу')
    print('1 - Закрыть программу')
    status = int(input())
    print(' ')
    if status == 0:
        print('Введите два числа')
        a=float(input())
        b=float(input())
        c=a+b
        d=a-b
        e=abs((a+b))/2
        g=a*b
        h=a/b
        print('Ответы:')
        print("Сумма =",c)
        print("Разность =", d)
        print("Среднее арифметическое =", e)
        print("Произведение =", g)
        print("Частное =", h)

