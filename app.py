from flask import Flask
app = Flask(__name__)



def send(message):
  print(message)

def get():
  return input(f"\nDigite a mensagem: ")



if __name__ == '__main__':
  send('ola Seja bem vindo')
  print(get())
