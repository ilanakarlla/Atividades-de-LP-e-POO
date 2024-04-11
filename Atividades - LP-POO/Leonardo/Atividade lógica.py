'''
for i in range (11):
    print(i)
#2

condicao = int(input('Digite 1 se quiser ver os números de 0 até 10 ou 2 se não: '))
if condicao == 1:
    for i in range(11):
      print(i)
else:
    print('Você não deseja ver os números!')

'''

#3, 4 e 5 e 6:

parada = False

while not parada:
    condicao = input("""
-------------------- Menu de opções --------------------
    
    Digite 1 se quiser ver a sequência de 1 até 10
    Digite 2 se quiser criar uma contagem personalizada 
    Digite 3 se quiser sair do programa
    Digite 4 para visualizar os números primos
    
-------------------- Fim das opções --------------------

Insira uma opção: """)

    try:
        condicao = int(condicao)

        if condicao == 1:
            for i in range(1, 11):
                print(i)

        elif condicao == 2:
            numDois = input('Digite um número para que sua sequência seja formada até o mesmo: ')
            try:
                numDois = int(numDois)
                for i in range(1, numDois + 1):
                    print(i)
            except ValueError:
                numCerto = input('O valor inserido é inválido. Por favor, insira um número válido: ')
                numCerto = int(numCerto)
                for i in range(numCerto):
                    print(i + 1)
        elif condicao == 3:
            parada = True

        elif condicao == 4:
            numQuatro = input('Digite um número para que sua sequência de números primos seja formada até o mesmo: ')
            try:
                a = False
                numQuatro = int(numQuatro)
                for i in range(1, numQuatro + 1):
                    if i != 2:
                        for j in range(2, i):
                            if i % j == 0:
                                a = True
                    else:
                        a = True
                    if not a:
                        print(i)
                    a = False

            except ValueError:
                numCerto = input('O valor inserido é inválido. Por favor, insira um número válido: ')
                numCerto = int(numCerto)
                for i in range(numCerto):
                    print(i + 1)
        else:
            numTres = input('O valor inserido é inválido. Digite um valor válido: ')
            try:
                numTres = int(numTres)
                for i in range(1, numTres + 1):
                    print(i)
            except ValueError:
                numCerto = input('O valor inserido é inválido. Por favor, insira um número válido: ')
                numCerto = int(numCerto)
                for i in range(numCerto):
                    print(i + 1)

    except ValueError:
        numCerto = input('O valor inserido é inválido. Por favor, insira um número válido: ')
        numCerto = int(numCerto)
        for i in range(numCerto):
            print(i + 1)