import random
import sources as src
import os
from datetime import datetime
from dotenv   import load_dotenv
from datetime import timedelta  


load_dotenv()



def send(message):
  print(message)

def get(user ='', validation=False, message=''):
  if(validation):
    send(message)
    userIntput = input(f'{user}: ')
    userIntput = userIntput.upper()

    lowerThanA    = ord(userIntput) < options()['begin']
    upperThanX    = ord(userIntput) > options()['end']
    moreThan1Char = len(userIntput)>1

    if(moreThan1Char or lowerThanA or upperThanX):
      get(True, 'Opcao incorreta, digite somente o index (A, B, C...)')

    return userIntput
  else: 
    return input('Digite: ')

def options():
  return {
    "begin" : 65,
    "end"   : 65+int(os.getenv('OPTIONS'))
  } 

def getToken():
  return str(os.getenv('TOKEN'))

def shuffleAndReturn(questions):
  random.shuffle(questions)
  return questions[:int(os.getenv('QUESTIONS'))]

def format(options):
  ascii = 65
  formattedText = ''
  formattedOptions = []

  for option in options:
    formattedText += f'\n{chr(ascii)}: {option}'
    formattedOptions.append(
      {
        'text' : f'{option}',
        'letter' : f'{chr(ascii)}'
      }
    )
    ascii += 1

  formatted = {
    "text" : formattedText,
    "details" : formattedOptions
  }   
  return formatted


def createOptionsForNumbers(number):
  numberOfOptions = int(os.getenv('OPTIONS'))
  options = []

  for x in  range(numberOfOptions-1):
    initialSeed = random.randint(5, 15)
    finalSeed   = random.randint(17, 30)
    rp = random.randint(initialSeed, finalSeed)
    if(x > (x/2)):
      choice = ((number*(rp/100)) + number)
    else:
      choice = (number - (number*(rp/100)))
    
    options.append(int(choice))

  options.append(number)
  random.shuffle(options)
  return options


def createOptionsForDates(date):
  numberOfOptions = int(os.getenv('OPTIONS'))
  options = []

  date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S%z")
  options.append(date.strftime('%Y-%d-%m'))
  
  for x in range(numberOfOptions-1):
    daySeed1     = random.randint(1, 13)
    daySeed2     = random.randint(15, 28)
    daySeed      = random.randint(daySeed1, daySeed2)

    if(x > (x/2)):
      choice = date + timedelta(days=-daySeed)
    else:
      choice = date + timedelta(days=+daySeed)

    options.append(choice.strftime('%Y-%d-%m'))

  random.shuffle(options)
  return options

  
def createOptionsForCountries(country):
  numberOfOptions = int(os.getenv('OPTIONS'))
  options = []
  options.append(country)

  countries = src.getCountries()

  for x in range(numberOfOptions-1):
    seed = random.randint(1, len(countries))
    choice = countries[seed]
    options.append(choice['Country'])

  random.shuffle(options)
  return options
