### WAP to check if a string represents even or odd number. ignore position of 1 '-' symbol.
num = input('Enter a string: ')
try:
    if (num.isdigit()) | ((num.replace('-','',1).isdigit())):
        num = int(num)
        if num%2 == 0:
            print("{} is an even number.".format(num))
        else:
            print("{} is an odd number.".format(num))
    else:
        raise ValueError('Raising Exception Manually 1')

except Exception as e:
    try:
        if (num[-1]=='-') & (num.count('-') == 1):
            num = int(num.replace('-',''))
            if num%2 == 0:
                print("{}- is an even number.".format(num))
            else:
                print("{}- is an odd number.".format(num))
        else:
            raise ValueError('Raising Exception Manually 2')
    except IndexError:
        print('Error: String is blank.')
    except Exception as e:
        print(e)
