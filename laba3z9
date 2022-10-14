n, f, s = map(float, input('n, f, s = ').split())
if s != 0:
    if n == f:
        print('Нет')
    else:
        if s<0:
            f, n = n, f
            s = abs(s)
        while f<n:
            f += s
        print('Да' if n == f else 'Нет')
else:
    print('Да' if n == f else 'Нет')
