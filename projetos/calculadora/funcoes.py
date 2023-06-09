
def soma(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        retorno = f'\nO resultado da soma {a} + {b} é {a + b}.'
        return retorno     
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser numéricos, recebido a={a} tipo({type(a)}, b={b} tipo({type(b)})")

def subtracao(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        retorno = f'\nO resultado da subtracao {a} - {b} é {a - b}.'
        return retorno     
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser numéricos, recebido a={a} tipo({type(a)}, b={b} tipo({type(b)})")

def multiplicacao(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        retorno = f'\nO resultado da multiplicação {a} x {b} é {a * b}.'
        return retorno     
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser numéricos, recebido a={a} tipo({type(a)}, b={b} tipo({type(b)})")


def divisao(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        retorno = f'\nO resultado da divisão {a} / {b} é {a / b}.'
        return retorno     
    else:
        raise TypeError(f"O input 'a' e 'b' devem ser numéricos, recebido a={a} tipo({type(a)}, b={b} tipo({type(b)})")
