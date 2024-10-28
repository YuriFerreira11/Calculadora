#menu
def calculate():
    operação = input('''Escolha sua operação matemática 
1 para adição
2 para subtração
3 para multiplicação
4 para divisão
''')
    
    # Caso digita maior q 4, volta para o menu

    if operação.isdigit() and int(operação) >= 5:
         print("Você digitou um número errado")
         calculate() 

    n1 = int(input ("Insira o primeiro número "))
    n2 = int(input ("Insira o segundo número "))
    
    #adição
    if operação == "1":
          print("{} + {} = ".format(n1, n2))
          print(n1 + n2)

    #substituição
    elif operação == "2":
          print("{} - {} = ".format(n1, n2))
          print(n1 - n2)
    
    #multiplicação
    elif operação == "3":
          print("{} * {} = ".format(n1, n2))
          print(n1 * n2)

    #divisão
    elif operação == "4":
          
          if n2 == 0:
               print("Erro, não é possivel dividir por 0")
          else:
               print("{} / {} = ".format(n1, n2))
               print(n1 / n2)
    #sem opção
    else:
         print("Escolha incorreta, por favor reinicie")
         calculate()
    again()
    return
   #Repetição da conta
def again():
    print("Você quer repetir sua conta?")
    calc_again = input('''Você quer calcular novamente?
                        Escolha S para sim ou N para não ''')
    if calc_again.upper() == "S":
        calculate()
    elif calc_again.upper() == "N":
        print("Obrigado por ter vindo")
        return 
    else:
        print("Opção errada!")
        again()

calculate()