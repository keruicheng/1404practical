import random



def main():
    total_picks = int(input('How many quick picks?'))
    for l in range(total_picks):
        numbers()



def numbers():
    constants = []
    while len(constants) < 6:
        tempInt = random.randint(1,45)
        if tempInt not in constants:
            constants.append(tempInt)
    constants.sort()
    print(constants)
    if len(constants) > 6:
        constants = []

main()