from functions import salary,hello_who

#print(hello_who('Max'))

if salary != 20:
    print('ERROR')
if hello_who('Max') != 'Hello,Max':
    print('LOX')
else:
    print('NICE')
if hello_who('Leo') != 'Hello,Leo':
    print('FAILED')
else:
    print('GOOD')