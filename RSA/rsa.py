import math
import random
import convert
import os


def simple_test(z):
    flag = 0
    if z % 2 == 0:
        return False
    for i in range(3, ((math.ceil(math.sqrt(z))) + 1), 2):
        if z % i == 0:
            flag = 1
            break
    if flag == 0:
        return True
    else:
        return False


def create():
    p1 = random.randint(int(10 ** 5), int((10 ** 6) - 1))
    while (simple_test(p1) != True):
        p1 = random.randint(int(10 ** 5), int((10 ** 6) - 1))
    p2 = random.randint(int(10 ** 5), int((10 ** 6) - 1))
    while (simple_test(p2) != True) or (len(str(p2)) != len(str(p1))):
        p2 = random.randint(int(10 ** 5), int((10 ** 6) - 1))
    n = p1 * p2
    phi = (p1 - 1) * (p2 - 1)
    e = 1
    while True:
        e += 2
        if (phi % e != 0):
            break
    k = 1
    while True:
        k += 1
        d = ((k * phi) + 1) / e
        if (d == int(d)):
            d = int(d)
            break
    outputs = open('public.key', 'w')
    outputs.write(str(e) + '\n')
    outputs.write(str(n) + '\n')
    outputs.close()
    outputs = open('private.key', 'w')
    outputs.write(str(d) + '\n')
    outputs.write(str(n) + '\n')
    outputs.close()
    print('You\'re keys have been generated in', os.getcwd())


def encrypt():
    print('Pick the file you want to encrypt', end='\n')
    while True:
        print('Type the name of file (it must be in ', os.getcwd(), '): ', end='', sep='')
        inp = input()
        try:
            inputs = open(inp, 'r')
        except:
            print('Sorry! We can\'t find this file! Try again!', end='\n')
            continue
        else:
            print('Successfully opened file "{}"'.format(inp))
            break
    del(inp)
    print('\n' + 'Now, choose the public key')
    while True:
        print('Type the name of file (it must be in ', os.getcwd(), '): ', end='', sep='')
        key = input()
        try:
            okey = open(key, 'r')
        except:
            print('Sorry! We can\'t find this file! Try again!', end='\n')
            continue
        else:
            print('Successfully opened file "{}"'.format(key))
            break
    del(key)
    b = inputs.read()
    inputs.close()
    i = -1
    a = []
    c = []
    message = ''
    try:
        while True:
            i += 1
            a.append(b[i])
    except:
        pass
    for i in range(0, len(a), 1):
        c.append(convert.convert(a[i]))
    for i in range(0, len(c), 1):
        message += c[i]
    d = okey.read().split('\n')
    print(message)
    encr = 0
    message = int(message)
    encr = pow(message, d[0], d[1])
    inp = inp + '_encrypted'
    outputs = open(inp, 'w')
    outputs.write(str(encr))
    outputs.close()
    print('File was successfully encrypted (encrypted file: "', inp, '")',  end='\n', sep='')


def decrypt():
    print('Pick the file you want to decrypt', end='\n')
    while True:
        print('Type the name of file (it must be in ', os.getcwd(), '): ', end='', sep='')
        inp = input()
        try:
            inputs = open(inp, 'r')
        except:
            print('Sorry! We can\'t find this file! Try again!', end='\n')
            continue
        else:
            print('Successfully opened file "{}"'.format(inp))
            break
    print('\n' + 'Now, choose the private key')
    while True:
        print('Type the name of file (it must be in ', os.getcwd(), '): ', end='', sep='')
        key = input()
        try:
            pkey = open(key, 'r')
        except:
            print('Sorry! We can\'t find this file! Try again!', end='\n')
            continue
        else:
            print('Successfully opened file "{}"'.format(key))
            break
    b = inputs.read()
    inputs.close()
    c = pkey.read().split('\n')
    m = []
    d = int(c[0])
    n1 = int(c[1])
    b = int(b)
    message = pow(b, d, n1)
    message = str(message)
    inp = inp + '_decrypted'
    outputs = open(inp, 'w')
    for i in range(3, len(message) + 1, 3):
        m.append(convert.convert(message[i - 3:i]))
    for i in range(0, len(m), 1):
        outputs.write(m[i])
    outputs.close()
    print('File was successfully decrypted (decrypted file: "', inp, '")', end='\n', sep='')


def main():
    print("""
Welcome to our simple RSA-like encryptor
  
Choose one of the options:

1) Create a pair of keys (public.key and private.key)
2) Encrypt the file
3) Decrypt the file""")
    func = int(input('>> '))
    if (func == 1):
        create()
    elif (func == 2):
        encrypt()
    elif (func == 3):
        decrypt()


if __name__ == '__main__':
    main()