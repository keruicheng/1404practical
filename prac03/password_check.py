Min_length = 6

def main():
    password = input_password(Min_length)
    asterisks(password)

def input_password(min_length):
    password = input('Please enter a password more than {} characters:'.format(Min_length))

    while len(password) < Min_length:
        print('Your password is too short')
        password = input('Please enter a password more than {} characters.'.format(Min_length))
    return password

def asterisks(length):
    print('*' * len(length))

main()