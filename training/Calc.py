import math
import os

def firsta(string):
    global a
    try:
        a = float(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        firsta(string)
def secondb(string):
    global b
    try:
        b = float(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        secondb(string)
def inta(string):
    global a
    try:
        a = int(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        inta(string)
def anfunc(string):
    global an
    try:
        an = float(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        anfunc(string)
def a1func(string):
    global a1
    try:
        a1 = float(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        a1func(string)
def dfunc(string):
    global d
    try:
        d = float(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        dfunc(string)
def nfunc(string):
    global n
    try:
        n = int(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        nfunc(string)
def bnfunc(string):
    global bn
    try:
        bn = float(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        bnfunc(string)
def b1func(string):
    global b1
    try:
        b1 = float(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        b1func(string)
def qfunc(string):
    global q
    try:
        q = float(input(string))
    except ValueError:
        print('| Big mistake, try again!!!')
        qfunc(string)
ex1 = 0
ex2 = 0
func = 0
print("""
 -----------------------------------------------------------
|     >> This program was fully writed by @anton2920 <<     |
|      ▁▂▃▄▅▆▇ ⒸⒶⓁⒸⓊⓁⒶⓉⓄⓇ ⓇⓊⒷⒾⒹⒾⓊⓂ ▇▆▅▄▃▂▁       |           
 -----------------------------------------------------------""")
while True:
 if ex1 == 1:
     os.system('cls' if os.name == 'nt' else 'clear')
     break
 else:
   func = 0
   ex1 = 0
   ex2 = 0
   print("""
 ----------------------------------------------------------- 
|                                                           |
|                     >> MAIN MENU <<                       |
|                                                           |
|       1)Arithmetical tasks                                |
|       2)Complicated tasks                                 |
|       3)Trigonometry tasks                                |
|       4)Progression tasks                                 |
|                                                           |
|       >> Type "quit" to terminate this program <<         |
|                                                           |    """)
   func = input('|  Answer: ')
   print('|                                                           |')
   print(' -----------------------------------------------------------')
   if func == 'quit':
       print()
       os.system('cls' if os.name == 'nt' else 'clear')
       break
   elif func == '1':
       print()
       firsta('| Type a first number: ')
       while True:
          znak = input('| Type a math sign: ')
          if znak != '+' and znak != '-' and znak != '*' and znak != '/':
             print('| Error!!! Unknown math sign')
          else: break
       secondb('| Type a second number: ')
       if znak == '+':
          c = a + b
       elif znak == '-':
          c = a - b
       elif znak == '*':
          c = a * b
       elif znak == '/':
          if b != 0:
             c = a / b
          else:print('| Error!!! You cannot divide by 0!!! (At least in this calculator)')
       print()   
       print('|  Answer: ', c)
       print()
       print(' -----------------------------------------------------------')
       print()
       func = ''
       ex1 = 0
       while True:
          func = input('>> Continue? [Y/n] ')
          if func == 'n' or func == 'N':
             ex1 = 1
             print()
             print(' -----------------------------------------------------------')
             print()
             break
          elif func == 'y' or func == 'Y' or func == '':
             break
          else:
             print('| Big mistake, try again!!!')
       if ex1 == 1:
          break
   elif func == '2':
       while True:
           print("""|                                                           |
|                 >> Complicated tasks <<                   |
|                                                           |
|       1)Math power                                        |
|       2)Math root                                         |
|       3)Show pi (With accuracy 31 decimal places)         |
|       4)Factorial                                         |
|                                                           |
|       >> Type "back" to go to the previous menu <<        |
|       >> Type "quit" to terminate this program <<         |
|                                                           |""")
           func = input('|  Answer: ')
           print('|                                                           |')
           print(' -----------------------------------------------------------')
           if func == 'back':
               break
           elif func == 'quit':
               print()
               ex1 = 1
               break
           elif func == '1':
               print()
               firsta('| Type a number: ')
               secondb('| Type a power: ')
               c = a ** b
           elif func == '2':
               print()
               firsta('| Type a number: ')
               secondb('| Type a root power: ')
               c = a ** (1/b)
           elif func == '3':
               print()
               print('| Pi = 3.1415926535897932384626433832795');
               print()
               c = 0
           elif func == '4':
               print()
               inta('| Type a number: ')
               c = 1
               for b in range (a, 0, -1 ):
                   c = c * b
           else:
               print()
               print('| Big mistake, try again!!!')
               print()
               print(' -----------------------------------------------------------')
               continue
           if c:
                  print()
                  print('|  Answer: ', c)
                  print()
                  print(' -----------------------------------------------------------')
                  print()
                  while True:
                      func = input('>> Continue? [Y/n] ')
                      if func == 'n' or func == 'N':
                          ex1 = 1
                          print()
                          print(' -----------------------------------------------------------')
                          print()
                          break
                      elif func == '' or func == 'y' or func == 'Y':
                          ex2 = 1
                          break
                      else:
                          print('| Big mistake, try again!!!')
                  if ex1 == 1 or ex2 == 1:
                      break
           else:
                   print(' -----------------------------------------------------------')
                   print()
                   func = ''
                   ex1 = 0
                   ex2 = 0
                   while True:
                       func = input('>> Continue? [Y/n] ')
                       if func == 'n' or func == 'N':
                           ex1 = 1
                           print()
                           print(' -----------------------------------------------------------')
                           print()
                           break
                       elif func == '' or func == 'y' or func == 'Y':
                           ex2 = 1
                           break
                       else:
                           print('| Big mistake, try again!!!')
                   if ex1 == 1 or ex2 == 1:
                       break
   elif func == '3':
       while True:
           print("""|                                                           |
|               >> Trigonomethrical tasks <<                |
|                                                           |
|       1)SIN                                               |
|       2)COS                                               |
|       3)TAN                                               |
|       4)CTAN                                              |
|                                                           |
|       >> Type "back" to go to the previous menu <<        |
|       >> Type "quit" to terminate this program <<         | 
|                                                           |""")
           func = input('|  Answer: ')
           print('|                                                           |')
           print(' -----------------------------------------------------------')
           if func == 'back':
               break
           elif func == 'quit':
               print()
               ex1 = 1
               break
           elif func == '1':
               print()
               firsta('| Type a degree: ')
               b = a * math.pi / 180
               c = math.sin(b)
           elif func == '2':
               print()
               firsta('| Type a degree: ')
               b = a * math.pi / 180
               c = math.cos(b)
           elif func == '3':
               print()
               firsta('| Type a degree: ')
               b = a * math.pi / 180
               c = math.tan(b)
           elif func == '4':
               print()
               firsta('| Type a degree: ')
               b = a * math.pi / 180
               c = math.cos(b) / math.sin(b)
           else:
               print()
               print('| Big mistake, try again!!!')
               print()
               print(' -----------------------------------------------------------')
               continue
           print()
           print('|  Answer: ', round(c,2))
           print()
           print(' -----------------------------------------------------------')
           print()
           func = ''
           ex1 = 0
           while True:
               func = input('>> Continue? [Y/n] ')
               if func == 'n' or func == 'N':
                   ex1 = 1
                   print()
                   print(' -----------------------------------------------------------')
                   print()
                   break
               elif func == '' or func == 'y' or func == 'Y':
                   ex2 = 1
                   break
               else:
                   print('| Big mistake, try again!!!')
           if ex1 == 1 or ex2 == 1:
               break
   elif func == '4':
       while True:
           if ex1 == 1 or ex2 == 1:
               break
           else:
               print("""|                                                           |
|                  >> Progression tasks <<                  |
|                                                           |
|       1)Arithmetical progression                          |
|       2)Geometry progression                              |
|                                                           |
|       >> Type "back" to go to the previous menu <<        |
|       >> Type "quit" to terminate this program <<         |
|                                                           |""")
               func = input('|  Answer: ')
               print('|                                                           |')
               print(' -----------------------------------------------------------')
               if func == 'back':
                   break
               elif func == 'quit':
                   print()
                   ex1 = 1
                   break
               elif func == '1':
                   while True:
                       if ex1 == 1 or ex2 == 1:
                           break
                       else:
                           print("""|                                                           |
|              >> Arithmetical progression <<               |
|                                                           |
|       1)Find a specific progression member                |
|       2)Find sum of "n" first progression members         |
|                                                           |
|       >> Type "back" to go to the previous menu <<        |
|       >> Type "quit" to terminate this program <<         |
|                                                           |""")
                           func = input('|  Answer: ')
                           print('|                                                           |')
                           print(' -----------------------------------------------------------')
                           if func == 'back':
                               break
                           elif func == 'quit':
                               print()
                               ex1 = 1
                               break
                           elif func == '1':
                               print()
                               a1func('| Type a1: ')
                               dfunc('| Type d: ')
                               nfunc('| Type a number: ')
                               an = a1 + ((n - 1) * d)
                               print()
                               print ('|  Answer: number "{}" = {}'.format(n, an))
                               print()
                               print(' -----------------------------------------------------------')
                               print()
                               while True:
                                   func = input('>> Continue? [Y/n] ')
                                   if func == 'n' or func == 'N':
                                       ex1 = 1
                                       print()
                                       print(' -----------------------------------------------------------')
                                       print()
                                       break
                                   elif func == '' or func == 'y' or func == 'Y':
                                       ex2 = 1
                                       break
                                   else:
                                       print('| Big mistake, try again!!!')
                               if ex1 == 1 or ex2 == 1:
                                   break
                           elif func == '2':
                               while True:
                                   if ex1 == 1:
                                       break
                                   else:
                                       print("""|                                                           |     
|         >> Sum of "n" first progression members <<        |
|                                                           |
|       Which formula?                                      |
|       1)Sn = ((a1 + an) * n) / 2                          |
|       2)Sn = (((2 * a1) + (d * (n - 1))) * n) / 2         |
|                                                           |
|       >> Type "back" to go to the previous menu <<        |
|       >> Type "quit" to terminate this program <<         |
|                                                           |""")
                                       func = input('|  Answer: ')
                                       print('|                                                           |')
                                       print(' -----------------------------------------------------------')
                                       if func == 'back':
                                           break
                                       elif func == 'quit':
                                           print()
                                           ex1 = 1
                                           break
                                       elif func == '1':
                                           print()
                                           a1func('| Type a1: ')
                                           anfunc('| Type an: ')
                                           nfunc('| Type a number: ')
                                           s = ((a1 + an) * n) / 2
                                       elif func == '2':
                                           a1func('| Type a1: ')
                                           dfunc('| Type d: ')
                                           nfunc('| Type a number: ')
                                           s = (((2 * a1) + (d * (n - 1))) * n) / 2
                                       else:
                                           print()
                                           print('| Big mistake, try again!!!')
                                           print()
                                           print(' -----------------------------------------------------------')
                                           continue
                                       print()
                                       print('|  Answer: sum of first "{}" numbers = {}'.format(n,s))
                                       print()
                                       print(' -----------------------------------------------------------')
                                       print()
                                       while True:
                                           func = input('>> Continue? [Y/n] ')
                                           if func == 'n' or func == 'N':
                                               ex1 = 1
                                               print()
                                               print(' -----------------------------------------------------------')
                                               print()
                                               break
                                           elif func == '' or func == 'y' or func == 'Y':
                                               ex2 = 1
                                               break
                                           else:
                                               print('| Big mistake, try again!!!')
                                       if ex1 == 1 or ex2 == 1:
                                           break
                           else:
                               print()
                               print('| Big mistake, try again!!!')
                               print()
                               print(' -----------------------------------------------------------')
                               continue
               elif func == '2':
                   while True:
                       if ex1 == 1 or ex2 == 1:
                           break
                       else:
                           print("""|                                                           |             
|                >> Geometry progression <<                 |
|                                                           |
|       1)Find a specific progression member                |
|       2)Find sum of "n" first progression members         |
|                                                           |
|       >> Type "back" to go to the previous menu <<        | 
|       >> Type "quit" to terminate this program <<         |
|                                                           |""")
                           func = input('|  Answer: ')
                           print('|                                                           |')
                           print(' -----------------------------------------------------------')
                           if func == 'back':
                               break
                           elif func == 'quit':
                               ex1 = 1
                               print()
                               break
                           elif func == '1':
                               print()
                               a1func('| Type a1: ')
                               qfunc('| Type q: ')
                               nfunc('| Type a number: ')
                               an = a1 * (q ** (n - 1))
                               print()
                               print('|  Answer: number "{}" = {}'.format(n, an))
                               print()
                               print(' -----------------------------------------------------------')
                               print()
                               while True:
                                   func = input('>> Continue? [Y/n] ')
                                   if func == 'n' or func == 'N':
                                       ex1 = 1
                                       print()
                                       print(' -----------------------------------------------------------')
                                       break
                                   elif func == '' or func == 'y' or func == 'Y':
                                       ex2 = 1
                                       break
                                   else:
                                       print('| Big mistake, try again!!!')
                               if ex1 == 1 or ex2 == 1:
                                   break
                           elif func == '2':
                               print()
                               b1func('| Type b1: ')
                               qfunc('| Type q: ')
                               nfunc('| Type a number: ')
                               s = (b1 * ((q ** n) - 1)) / (q - 1)
                           else:
                               print()
                               print('| Big mistake, try again!!!')
                               print()
                               print(' -----------------------------------------------------------')
                               continue
                           print()
                           print('|  Answer: sum of first "{}" numbers = {}'.format(n,s))
                           print()
                           print(' -----------------------------------------------------------')
                           print()
                           while True:
                               func = input('>> Continue? [Y/n] ')
                               if func == 'n' or func == 'N':
                                   ex1 = 1
                                   print()
                                   print(' -----------------------------------------------------------')
                                   print()
                                   break
                               elif func == '' or func == 'y' or func == 'Y':
                                   ex2 = 1
                                   break
                               else:
                                   print('| Big mistake, try again!!!')
                           if ex1 == 1 or ex2 == 1:
                               break
               else:
                   print()
                   print('| Big mistake, try again!!!')
                   print()
                   print(' -----------------------------------------------------------')
                   continue
   else:
       print()
       print('| Big mistake, try again!!!')
       continue
