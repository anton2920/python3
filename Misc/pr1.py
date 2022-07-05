b=1
c=1
b1=1
c1=1
d=1
ans=0
x1=0
def factorial(a):
   global d
   global fact
   for i in range(1,a+1,1):
      d=d*i
   fact = d
   d = 1
   return fact
def first():
   global b
   global c
   for j in range(1,2017,2):
      b=b*j
   for j in range(2,2018,2):
      c=c*j
   return b/c
def second():
   global b1
   global c1
   global x1
   b1 = factorial(2016)
   c1 = (2**2016) * factorial(1007) * factorial(1009)
   return b1/c1
if first() > second():
   print('Yes')
   b = 1
   c = 1
   b1 = 1
   c1 = 1
   d = 1
   x1 = 0
   ans = first() - second()
   b = 1
   c = 1
   b1 = 1
   c1 = 1
   d = 1
   x1 = 0
   ans = ans / second()
   print(ans)
else:
   print('No')
   b=1
   c=1
   b1=1
   c1=1
   d=1
   x1=0
   ans = (second()-first()) / first()
   print(ans)
