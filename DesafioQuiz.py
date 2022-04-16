print('=' * 30, 'DESAFIO QUIZ', '=' * 30)

print('''
A música 'Piece of me' da Britney Spears,
é uma crítica sobre...
1 - Ao assédio da imprensa
2 - À traição no casamento
3 - Ao machismo
4 - Aos abusos sexuais

  [150 mil] [300 mil] [400 mil]
   ERRAR     PARAR     ACERTAR
''')
resposta = input().lower()

if resposta == "1":
    print("Acertou - Ganhou 400 mil :) ")
elif resposta == "2":
    print("Errou - vai levar só 150 mil :( ")
elif resposta == "3":
    print("Errou - vai evar só 150 mil :( ")
elif resposta == "4":
    print("Errou - vai levar só 150 mil :( ")
elif resposta == "parar":
    print("Que Pena - vai levar só 300 mil :( ")

