import os
import sys
sys.path.insert(0,os.getcwd())

from projetos.calculadora import calcule
from projetos.calculadora import calcule2

from funcoes import soma

while True:
    print('Caculadora:')
    print('===========')
    print('            1) Soma')
    print('            2) Subtração')
    print('            3) Multiplicação')
    print('            4) Divisão')
    print('            0) Sair')
    opcao = input('Digite a sua opção: ')
    if opcao not in ('1', '2', '3', '4', '0'):        
        continue
    if opcao == '0':
        break
    while True:
        try:
            x = float(input('Digite o primeiro número: '))
        except:
            print('Número digitado inválido!')
            continue
        try:
            y = float(input('Digite o segundo número: '))
        except:
            print('Número digitado inválido!')
            continue
        operacao = soma
        if opcao == '1':
            calcule2(x,y,operacao)
        calcule()
print('Programa finalizado!!')