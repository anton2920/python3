def main():
	c = input('Type your FIO: ')
	a = c.split()
	b = a[0] + ' ' + a[1][0] + '.' + a[2][0] + '.'
	print(b, end='\n')


if __name__ == '__main__':
	main()
