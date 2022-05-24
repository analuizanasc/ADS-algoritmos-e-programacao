''' Aluna: Ana Luiza Araújo do Nascimento
Matrícula: 2022111590084
Curso: Análise e desenvolvimento de sistemas
Disciplina: Algoritmos e programação
>TED:'''

from time import sleep


def media_aritmetica():
    ma = (valor1 + valor2 + valor3) / 3
    print(f'\033[32mA média aritmética é {ma:.2f}\033[m')


def media_ponderada():
    mp = ((valor1 * 5) + (valor2 * 3) + (valor3 * 2)) / (5 + 3 + 2)
    print(f'\033[32mA média ponderada é {mp:.2f}\033[m')


def media_harmonica():
    mh = 3 / ((1 / valor1) + (1 / valor2) + (1 / valor3))
    print(f'\033[32mA média harmônica é {mh:.2f}\033[m')


def main():
    while True:
        media = {
            'A': media_aritmetica,
            'P': media_ponderada,
            'H': media_harmonica,
        }
        funcao = str(input(f'Que tipo de média você deseja calcular? '
                           f'\nA = Média aritmética'
                           f'\nP = Média ponderada'
                           f'\nH = Média harmônica'
                           f'\nDigite A, P ou H:')).upper().strip()[0]
        while funcao not in "APH":
            print('\033[31mDigite um valor válido!\33[m')
            funcao = str(input(f'Escolha a opção: '
                               f'\nA = Méia aritmética'
                               f'\nP = Média ponderada'
                               f'\nH = Média harmônica'
                               f'\nDigite A, P ou H:')).upper().strip()[0]
        media[funcao]()
        continuar = str(input('Deseja continuar? '
                              '\nDigite \033[32mS\033[m para sim ou qualquer tecla para sair:')).strip().upper()[0]
        if continuar == 'S':
            pass
        else:
            print('\033[32mObrigado por usar esse programa lindo!\033[m')
            break


print("\033[32mOlá, vamos calcular a média de três números?\033[m")
sleep(1)
print('-'*50)
valor1 = float(input('Digite o primeiro valor:'))
valor2 = float(input('Digite o segundo valor:'))
valor3 = float(input('Digite o terceiro valor:'))
print('-'*50)
main()
