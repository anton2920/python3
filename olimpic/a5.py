ans = 0
a = 1
n = int(input('Type n: '))
if (n>=1) and (n<30):
   for i in range (1, n+1, 1):
      a = a * i
   if a % 1000000 == 0:
      ans = 6
   elif a % 100000 == 0:
      ans = 5
   elif a % 10000 == 0:
      ans = 4
   elif a % 1000 == 0:
      ans = 3
   elif a % 100 == 0:
      ans = 2
   elif a % 10 == 0:
      ans = 1
   print(ans)
else: 
   print('Error!!!')
