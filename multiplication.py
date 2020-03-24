x = int(input('Введіть множник 1: '))
y = int(input('Введіть множник 2: '))

print('Результат множення:')

for num in range(1,y+1):
    z = x * num
    print(f'{x} x {num} = {z}')
