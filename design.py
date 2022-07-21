row = int(input('Enter the number of rows: '))
n = row
while n >= 0:
    x = '*' * n
    print(x)
    n -= 1

row = int(input('Enter the number of rows: '))
n = row
i = 1
while i <= n:
    print('*' * i)
    i += 1

row = int(input('Enter the number of rows: '))
n = row
while n >= 0:
    x = '*' * n
    y = ' ' * (row - n)
    print(y + x)
    n -= 1

row = int(input('Enter the number of rows: '))
n = row
i = 1
while i <= n:
    x = '*' * i
    y = ' ' * (row - i)
    print(y + x)
    i += 1