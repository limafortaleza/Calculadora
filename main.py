import operacoes
'''
Após vários dias tentando solucionar um erro dado no aplicativo da calculadora de um computador de uma empresa,
o técnico de TI e seu estagiário  decidiram fazer um código na linguagem Python que tivesse as funcionalidades de uma calculadora,
porém ao não obtiveram êxito nesse projeto. Para resolver esse problema lhe foi solicitado que você que desenvolvesse uma programa
de uma  calculadora em Python.Como você faria? Então desenvolva uma calculadora em Python que tenha como funções: soma, divisão,
subtração e adição, a calculadora tem que ter um menu para as operações e mostrar o resultado final. Além dessas funcionalidades
lhe foi solicitado que o arquivo principal do programa fosse diferente do(s) arquivo da funcionalidade da calculadora.
Importante: use o assunto de módulos e caso seja necessário suba a pasta dos arquivos da questão no drive e disponibilizando
o link da questão.
'''


print(' ')
print('=-'*10,'CALCULADORA','=-'*10)

while True:
    operacao = input("Selecione a operação desejada: \n"
                     "-------------------------------------- \n"
                     "Para SOMAR digite       -------> '+'\n"
                     "Para SUBTRAIR digite    -------> '-' \n"
                     "Para MULTIPLICAR digite -------> '*' \n"
                     "Para DIVIDIR digite     -------> '/' \n"
                     "--------------------------------------\n"
                     "Informe a operação: ")
    if operacao=="+":
        operacoes.sum()

    elif operacao == "-":
        operacoes.sub()

    elif operacao == "*":
        operacoes.multi()

    elif operacao == "/":
        operacoes.div()
    else:
        print("Operação inválida")
        break
