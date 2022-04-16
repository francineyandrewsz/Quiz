print('''

Seja bem-vindo ao jogo de perguntas e respostas.

Você tem 1 pergunta que vai dizer se você é um SURVIVOR.

''')
print('Vamos começar.')

print('O T-vírus foi desenvolvido por qual empresa?')
print('a) Umbrella')
print('b) Hospital de Nova York')
print('c) Academia dos S.T.A.R.S')

resposta = input('Digite uma das opções: ')
pontos = 0

if resposta == "a":
    print('Muito bem!')
    pontos += 1
else:
    print('tente novamente')

print('Sua pontuação final é', pontos)
