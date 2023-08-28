
def sum ():
    n1 = float(input("Digite o 1º numero: "))
    n2 = float(input("Digite o 2º numero: "))
    resultado=n1+n2
    print( f'Resultado: {resultado}')
    print('=-'*10)

def sub ():
    n1 = float(input("Digite o 1º numero: "))
    n2 = float(input("Digite o 2º numero: "))
    resultado=n1-n2
    print(f'Resultado: {resultado}')
    print('=-' * 10)

def div():
    n1 = float(input("Digite o 1º numero: "))
    n2 = float(input("Digite o 2º numero: "))
    if n2==0:
        print( 'Operação não é possível')
    else:
        resultado=n1/n2
        print(f'Resultado: {resultado}')
        print('=-' * 10)

def multi ():
    n1 = float(input("Digite o 1º numero: "))
    n2 = float(input("Digite o 2º numero: "))
    resultado = n1*n2
    print(f'Resultado: {resultado}')
    print('=-' * 10)
