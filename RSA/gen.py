outputs = open('gen.txt', 'w')
for i in range(200, 266, 1):
    #outputs.write('""' + ': ' + '"' + str(i) + '"' + ',' + '\n')
    outputs.write('"' + str(i) + '"' + ':' + ' ""' + ',' + '\n')
outputs.close()