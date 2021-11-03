from flask import Flask
app = Flask(__name__)



def send(message):
  print(message)

def get():
  return input('\nDigite a mensagem:')



if __name__ == '__main__':
  userInput = []
  questions = [
    'Qual foi a data do primeiro caso de COVID 19 no Brasil?',
    'Quantos casos confirmados tivemos hoje em todo o pais?',
    'Quantos casos confirmados no Brasil conseguiram se recuperar?',
    'Quantos casos confirmados no Brasil nao conseguiram se recuperar ate o momento?',
    'Quantos casos confirmados no Brasil evoluiram ao falecimento?',
    'Em 2020 o mundo presenciou quantas mortes por COVID 19?',
    'E do inicio de 2021 ate o momento, quantos ja vieram a falecer no mundo?',
    'Qual pais apresentou o maior indice de casos confirmados no mundo?',
    'Qual pais apresentou o maior indice de mortes no mundo?',
    'Quantos casos evoluiram a morte hoje no mundo?'
  ]

  for question in questions:
    send('\n'+question)
    userInput.append(get())

# criar classe para o quiz, objeto chamara pergunta e funcao response que irá verificar se está correta a resposta

