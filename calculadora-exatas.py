from math import *
from time import *

# EM DENSENVOLVIMENTO!!!!

# projeto calculadora automática
print('#POR FAVOR, DIGITE O NÚMERO CORRESPONDENTE#\n')
print('Olá! Seja bem vindo a Calculadora Automática do Matheus!!!🥰\nEm que área você deseja fazer seus cálculos??')
sleep(1)

# áreas de conhecimento
print('1- MATEMÁTICA\n2- FÍSICA\n3- CALCULADORA COMUM')
print('------------------------------')
materia = input('Digite uma área: ')

while True:
    if materia == '1':
        print('Cálculos disponíveis:\n1- Teoremas de Pitágoras\n2- Teorema de Bhaskara\n3- Áreas')
        print('------------------------------')
        sleep(1)
        calculo_math = input('Que cálculo devo resolver para você?🤩\n')

        # ESCOLHENDO O CÁLCULO A SER FEITO
        if calculo_math == '1':
            print('Dados disponíveis do triângulo retângulo:\n1- HIPOTENUSA E UM CATETO\n2- DOIS CATETOS')

            pitagoras_info = input('Informe os dados do seu triângulo!\n')

            # contem hipotenusa
            if pitagoras_info == '1':
                sleep(1)
                hipotenusa = int(input('* Digite o valor da hipotenusa(a): '))
                cateto_1 = int(input('* Digite o valor do cateto(b ou c): '))

                # cálculo do teorema de pitágoras
                cateto_descoberto = ((hipotenusa**2) - (cateto_1**2))**0.5
                cateto_descoberto = int(cateto_descoberto)
                print(f'O valor do outro cateto é:\n{cateto_descoberto}')
                print('------------------------------')
                continuar = input('Deseja continuar?(s/n) \n')

                if continuar == 'n':
                    print('Viu? Foi fácil!😅\nA gente se vê na próxima, GRANGE ABRAÇO!')
                    break
                else:
                    print('Ok, vamos continuar!')
                    continue

            # contem os dois catetos
            elif pitagoras_info == '2':
                sleep(1)
                cateto_b = int(input('Digite o valor do cateto(b): '))
                cateto_c = int(input('Digite o valor do outro cateto(c): '))

                # cálculo do da hipotenusa
                valor_hipotenusa = ((cateto_b**2) + (cateto_c**2))
                valor_hipotenusa = sqrt(valor_hipotenusa)
                print(f'O valor da hipotenusa é {valor_hipotenusa:.2f}!')                                               #corrigir depois a hipotenusa
                print('------------------------------')
                continuar = input('Deseja continuar?(s/n) \n')

                if continuar == 'n':
                    print('Viu? Foi fácil!😅\nA gente se vê na próxima, GRANGE ABRAÇO!')
                    break
                else:
                    print('Ok, vamos continuar!')
                    continue

        elif calculo_math == '2':
            print('Informe os dados da equação do 2° grau! (a, b e c):\n')
            print('#Se não houver a, b ou c, coloque como 0 (zero)#')
            sleep(1)
            a = int(input('A = '))
            b = int(input('B = '))
            c = int(input('C = '))

            #verificar delta
            delta = (b**2) - (4*a*c)

            if delta < 0:
                print('Não possui raizes reais!')
                continuar = input('Deseja continuar?(s/n) \n')

                if continuar == 'n':
                    print('Viu? Foi fácil!😅\nA gente se vê na próxima, GRANGE ABRAÇO!')
                    break
                else:
                    print('Ok, vamos continuar!')
                    continue

            elif delta == 0:                                                                                            #mostrar como delta foi montado futuramente
                x = -b / (2*a)
                print(f"X' = X'' = {x}")
                continuar = input('Deseja continuar?(s/n) \n')

                if continuar == 'n':
                    print('Viu? Foi fácil!😅\nA gente se vê na próxima, GRANGE ABRAÇO!')
                    break
                else:
                    print('Ok, vamos continuar!')
                    continue

            # Resolvendo Bhaskara
            else:
                x1 = ((-b) + sqrt(delta))/(2*a)
                x2 = ((-b) - sqrt(delta))/(2*a)
                print(f"X' = {x1}\nX'' = {x2}")
                continuar = input('Deseja continuar?(s/n) \n')

                if continuar == 'n':
                    print('Viu? Foi fácil!😅\nA gente se vê na próxima, GRANGE ABRAÇO!')
                    break
                else:
                    print('Ok, vamos continuar!')
                    continue
        elif calculo_math == '3':
            sleep(1)
            print('Eita... Chegamos na Geometria😅\nMas não se preocupe, vamos conseguir, veja os Cálculos de áreas disponíveis!!\n1- Triângulo\n2- Retângulo\n3- Circunferência\n4- Trapézio')
            #CONTINUAR AS ÁREAS
            pass
        else:
            print('Por favor, digite um número correspondente válido!')
    elif materia == '2':
        sleep(1)
        print('Vamos para a Física!😎')
        print('Cálculos disponíveis: \n1- Densidade\n2- Velocidade Média\n3- Pêndulos')
        print('------------------------------')
        break