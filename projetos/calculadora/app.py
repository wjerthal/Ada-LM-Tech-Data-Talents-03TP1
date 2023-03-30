import os
import sys
sys.path.insert(0,os.getcwd())

from projetos.calculadora import calcule

from funcoes import soma
from funcoes import subtracao
from funcoes import multiplicacao
from funcoes import divisao

while True:
    print('\nCaculadora:')
    print('===========')
    print('            1) Soma')
    print('            2) Subtração')
    print('            3) Multiplicação')
    print('            4) Divisão')
    print('            0) Sair')
    opcao = input('\nDigite a sua opção: ')
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
        if opcao == '1':
            operacao = soma
            print(calcule(x,y,operacao))
        if opcao == '2':
            operacao = subtracao
            print(calcule(x,y,operacao))
        if opcao == '3':
            operacao = multiplicacao
            print(calcule(x,y,operacao))       
        if opcao == '4':
            operacao = divisao
            print(calcule(x,y,operacao)) 
        break
print('Programa finalizado!!')