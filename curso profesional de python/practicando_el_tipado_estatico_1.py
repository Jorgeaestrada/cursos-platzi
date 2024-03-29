def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower
    return string == string[::-1]

def run():
    print(is_palindrome(1000))

if __name__ == '__main__':
    run()

"""
|################### RETO ######################|
|   Instalar el modulo mypy con el comando:     |
|   > pip install mypy                          |
|                                               |
|   ejecutar el script con el siguiente comando:|
|   > mypy .\palindrome.py --check-untyped-defs |
|###############################################|
"""