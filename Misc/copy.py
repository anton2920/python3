# Программа для копирования файлов!

print('This program creates backup of your selected file! Type "quit()" to exit')
file1 = input('Type the path of file: ')
def copy():
    global file1
    global file2
    inputs = open(file1, 'rb')
    file2 = file1 + '.backup'
    outputs = open(file2, 'wb')
    outputs.write(inputs.read())
    inputs.close()
    outputs.close()
    print('Compleated!')

if file1 != 'quit()':
    try:
        copy()
    except FileNotFoundError:
        print('Error! Unknown file!')
    finally:
        print('Bye!')
else:
    print('Bye!')