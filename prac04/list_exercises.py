numbers = []
total_numbers = 5

i = 0
while i < total_numbers:
    number = int(input('Number:'))
    numbers.append(number)
    i += 1

print('The first number is {}'.format(numbers[0]))
print('The last number is {}'.format(numbers[-1]))
print('The smallest number is {}'.format((min(numbers))))
print('The largest number is {}'.format((max(numbers))))
print('The average of the numbers is {}'.format(sum(numbers)/len(numbers)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input('Please enter the username:')
if username in usernames:
    print('Access granted')
else:
    print('Access denied')