# 10/0       # ZeroDivisionError: division by zero

# 1 + '1'   # TypeError: unsupported operand type(s) for +: 'int' and 'str'

while True:
    try:
        nome = input('Digite seu nome: ')
        print(f'Olá {nome}')
        0/0
    except KeyboardInterrupt:
        print('\nTudo Bemm já entendi, você não quer brincar')
        exit()
    except ZeroDivisionError:
        print('Você não sabe que não pode dividir por 0?')
        