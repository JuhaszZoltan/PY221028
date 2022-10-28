print('másodfokú egyenlet együtthatói: ')
a:float = float(input('a = '))
b:float = float(input('b = '))
c:float = float(input('c = '))

if a == 0:
    print('az egyenlet nem másodfokú!')
    print(f'x = {-c/b}')
else:
    d = b**2 - (4*a*c)
    if d < 0:
        print('nincs valós megoldás!')
    elif d == 0:
        print('egy megoldás van!')
        print(f'x = {-b/2*a}')
    else:
        print(f'xˇ1 = {(-b + d**.5) / (2*a)}')
        print(f'xˇ2 = {(-b - d**.5) / (2*a)}')