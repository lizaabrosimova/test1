a=int(input())
b = (a//10)%10
c = a%10
if b!=c:
  if b>c:
    print(b,'>', c)
  else:
    print(b,'<', c)
