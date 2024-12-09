try:
    num1=int(input('Enter any number: '))
    num2=int(input('Enter any number: '))
    result=num1/num2
    print('Result is: ', result)
    print('Result is: ', result1)

except ZeroDivisionError:
    print('Division by zero is not allowed in mathematics.')
except ValueError:
    print('Please put in integral values.')
except NameError as ex:
    print('Exception: ', ex)

except:
    print('Some weird error that no one knows about occured. Please try again.')
finally:
    print('I will execute this piece of code no matter what.')