a=int(input())
b=a//100%10
c=a//10%10
d=a%10
if b==c and c==d and d==b:
  print('Все цифры одинаковые')
else:
  print('Цифры разные')
