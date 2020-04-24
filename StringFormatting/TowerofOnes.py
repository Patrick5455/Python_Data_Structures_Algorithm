for i in range(2, 11):
    number_str = ''
    for j in range(1, i):
        number_str += str(j)

    number = int(number_str)
    ans = number * 9 + i
    print(f'{number:>10} x 9 + {i} = {ans}')

print(end ='')


for i in range(10, 1, -1):
    number_str = ''
    for j in range(1, i):
        number_str += str(j)

    number = int(number_str)
    ans = number * 9 + i
    print(f'{number:>10} x 9 + {i} = {ans}')