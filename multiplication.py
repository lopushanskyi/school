import random

r1_1 = 1
r1_2 = 10
r1 = random.randint(r1_1, r1_2)

r2_1 = 1
r2_2 = 10
r2 = random.randint(r2_1, r2_2)

answer = int(input(f'Скільки буде {r1} помножити на {r2}: '))

r3 = r1 * r2

while answer != r3:
    answer = int(input(f'Скільки буде {r1} помножити на {r2}: '))
    continue
else:
    print('you won')
