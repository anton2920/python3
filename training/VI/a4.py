def get_faculties(a):

    # Initializing variables
    i = len(a)
    j = 0
    dict = {}

    # Main part
    while i:
        ind = a[j].find(':')
        fac = a[j][ind + 2::]
        item = a[j][:ind]
        if fac not in dict.keys():
            c = []
            c.append(item)
            dict[fac] = c
        else:
            temp = []
            temp.append(item)
            temp2 = list(dict.pop(fac))
            for z in range(0, len(temp2)):
                temp.append(temp2[z])
            dict[fac] = temp

        i -= 1
        j += 1

    # Returning value
    return dict


def main():

    # Final output
    result = get_faculties(['Иван Иванов: физфак', 'Матвей Матвеев: филфак', 'Матвей Матвеев: физфак', 'Матвей Матвеев: филфак'])
    print(result)
    for key in sorted(result):
        print(key + ':', ', '.join(result[key]))


if __name__ == '__main__':
    main()
