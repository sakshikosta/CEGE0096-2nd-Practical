full_name = input('Please input your full name: ')
print(len(full_name))

n = int(input('Please enter an integer: '))
while n > 1 and n <= 7:
    if n == 1:
        print('Monday')
    elif n == 2:
        print('Tuesday')
    elif n == 3:
        print('Wednesday')
    elif n == 4:
        print('Thursday')
    elif n == 5:
        print('Friday')
    elif n == 6:
        print('Saturday')
    else:
        print('Sunday')
    n = int(input('Please enter an integer: '))
print('The provided integer does not correspond to a day!')