a=int(input())
if (a%2)<=0:
  if  a % 10 ==7:
    print("Четное оканчивается на 7")
  else:
    print("Четное не оканчивается на 7")
else:
  if  a % 10 ==7:
    print('Не является четным и оканчивается на 7')
  else:
    print('Не является четным и не оканчивается на 7')
