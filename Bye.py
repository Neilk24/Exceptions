valid=False

while not valid:
    try:
        n=int(input('Enter any number: '))
        while n%2==0:
            print('Bye')
            valid=True
    except ValueError as ex:
        print('Exception: ', ex)