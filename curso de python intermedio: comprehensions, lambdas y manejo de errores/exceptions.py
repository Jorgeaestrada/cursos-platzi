def palindrome(string):
    try:
        if(len(string) == 0):
            raise ValueError('no se puede ingresar una cadena vacía')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrome(''))
except TypeError:   
    print('sólo se pueden ingresar strings')