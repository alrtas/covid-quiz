from flask import Flask
import quiz
import helpers as hlp
app = Flask(__name__)



if __name__ == '__main__':
  
  hlp.send('Ola, seja bem vindo ao Quiz da COVID-19')
  hlp.send('Vamos comecar, digite o seu primeiro nome')
  user = hlp.get()
  user = user.capitalize()

  hlp.send(f'{user}, estou carregando seu jogo...')
  questions = quiz.questions

  for object in questions:
    hlp.send('\n'+object['question'])
    hlp.send(object['options']['text'])

    userInput = hlp.get(user, True)

    for option in object['options']['details']:
      if(option['letter'] == userInput):
        object['answer'] = option['text']

    if(object['answer'] == str(object['response'])):
      object['correct'] = True
    elif( (object['answer']+'T00:00:00Z') == object['response']):
      object['correct'] = True
    
  hlp.send('\nCalculando o seu resultado...')

  correct = 0
  total   = len(questions)
  for object in questions:
    if(object['correct'] == True):
      correct += 1

  hlp.send(f'\nVoce acertou {correct} de {len(questions)} totalizando uma nota de: {(correct/len(questions))*10} ')