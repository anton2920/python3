import os

print('Hello, this is the morse code to AB decryptor')
while True:
    print('Type the name of file (it must in', os.getcwd(), '): ', end='')
    a = input()
    try:
        inputs = open(a, 'r')
    except:
        print('Sorry! We can\'t find this file! Try again! ')
        continue
    else:
        print('Successfully opened file "{}"'.format(a))
        break
str = inputs.read()
inputs.close()
outputs = open('output.txt', 'w')
outputs.close()
outputs = open('output.txt', 'a')
for i in str:
    if i == "*":
        outputs.write('A')
    elif (i == "-") or (i == "_"):
        outputs.write('B')
outputs.close()
print('The result is written in "output.txt"')
print('Bye!')

