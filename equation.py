A1 = int(input())
A2 = int(input())
A3 = str(input('Оберіть дію: '))
A4 = int

B1 = int(input())
B2 = int(input())
B3 = str(input('Оберіть дію: '))
B4 = int

if A3 == '+':
    A4 = A1 + A2
    A3 = 'Сума'
elif A3 == '-':
    A4 = A1 - A2
    A3 = 'Різниця'
elif A3 == '/':
    A4 = A1 // A2
    A3 = 'Частка'
elif A3 == '*':
    A4 = A1 * A2
    A3 = 'Добуток'
else:
    print('Оберіть дію')

if B3 == '+':
    B4 = B1 + B2
    B3 = 'сумі'
elif B3 == '-':
    B4 = B1 - B2
    B3 = 'різниці'
elif B3 == '/':
    B4 = B1 // B2
    B3 = 'частці'
elif B3 == '*':
    B4 = B1 * B2
    B3 = 'добутку'
else:
    print('Оберіть дію')

if A4 == B4:
    print(A3, 'чисел', A1, 'i', A2, 'дорівнює', B3, 'чисел', B1, 'i', B2, sep=' ')
else:
    print(A3, 'чисел', A1, 'i', A2, 'не дорівнює', B3, 'чисел', B1, 'i', B2, sep=' ')
