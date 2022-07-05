def f(b):
   return ((4 * b ** 2) - (12 * b) - 27)
c = 0
for x in range (1, 2147483648, 1):
   a = f(x)
   if a < 0:
      a = a * (-1)
      m = 1
   for k in range (1, a+1, 1):
      if ((a % k == 0) and (a != k) and (k != 1)) or (a < 0) or (m == 1):
         c = 1
         break
   if c == 0:
      print(x, ' ')
   c = 0
   m = 0
