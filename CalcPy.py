import time
import os
while 1 != 2:
  print("Seja bem vindo a sua calculadora!")
  time.sleep(2)
  print("Utilize os seguintes comandos para as operações:")
  time.sleep(2)
  print(""" 
    SOMA          -> +
    SUBTRAÇÃO     -> -
    MULTIPLICAÇÃO -> *
    DIVISÃO       -> /
    POTÊNCIA      -> ^
  """)
  time.sleep(2)
  print("---------------------")
  time.sleep(0.7)
  
  soma = "+"
  sub = "-"
  multi = "*"
  divi = "/"
  poten = "^"
  zero = 0

  operation = str(input("Insira a operação: "))
  time.sleep(0.5)
  if operation == poten:
    numero1 = int(input("Insira o número da base: "))
    time.sleep(0.5)
    numero2 = int(input("Insira o número do expoente: "))
    print("\n{}^{} = ".format(numero1, numero2), numero1 **   numero2)
  
  if operation == soma:
    numero1 = int(input("Insira o primeiro número: "))
    time.sleep(0.5)
    numero2 = int(input("Insira o segundo número: "))
    time.sleep(0.5)
    print("\n{} + {} = ".format(numero1, numero2), numero1 +  numero2)
  
  elif operation == sub:
    numero1 = int(input("Insira o primeiro número: "))
    time.sleep(0.5)
    numero2 = int(input("Insira o segundo número: "))
    time.sleep(0.5)
    print("\n{} - {} = ".format(numero1, numero2), numero1 -  numero2)
  elif operation == multi:
    numero1 = int(input("Insira o primeiro número: "))
    time.sleep(0.5)
    numero2 = int(input("Insira o segundo número: "))
    time.sleep(0.5)
    print("\n{} X {} = ".format(numero1, numero2), numero1 *  numero2)

  if operation == divi:
    numero1 = int(input("Insira o primeiro número: "))
    numze = int(input("Insira o segundo número: "))
    if numze == zero:
      print("Ta loco? Não da pra dividir por zero, tente  denovo!! ")
    else:
      print("\n{} / {} = ".format(numero1, numze), numero1 /  numze)
  time.sleep(3)
  
  print('Deseja calcular outro número?')
  denovo = input('\nsim(y) ou Não(n)\n')
  if denovo == 'y':
    time.sleep(1)
    print('OK')
    time.sleep(3)
    os.system('clear')
  else:
    time.sleep(1)
    print('OK')
    time.sleep(2)
    print('Obrigado por usar a calculadora!!')
    break