

def retry(*args):
    calc_again = input("If you want to calculate again enter Y for Yes and N for No : ")
    if calc_again.upper() == "Y":
        return True
    elif calc_again.upper() == "N":
        return False
        
    else :
        return retry()
print(retry())

def calculator(*args):
    while True:
        N1 = int(input('Enter the first number: '))
        N2 = int(input('Enter the second number: '))

        operations = input('''
        Enter + for addition
        Enter - for subtraction
        Enter / for division
        Enter * for multiplication
        Enter z when the program isnt needed any longer
        ''')       

        add ='{} +{} = {}'.format(N1,N2,N1+N2)
        sub = '{} - {} = {}'.format(N1,N2,N1-N2)
        div = '{} / {} = {}'.format(N1,N2,N1/N2)
        mult = '{} * {} = {}'.format(N1,N2,N1*N2)

        if operations == '+' :
            print(add)
            if retry() == False:
                break
        elif operations == '-':
            print(sub)
            if retry() == False:
                break
        elif operations == '/':
            print(div)
            if retry() == False:
                break
        elif operations == '*':
            print(mult)
            if retry() == False:
                break
        else:
            print(' Please try again later ')
            break

#this will take the funtion back to the actual beginning again for the correct inputs
print(calculator())


    

