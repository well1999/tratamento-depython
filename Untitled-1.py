

credito = {'123': 750, '456': 812, '789': 980}
try:
  credito_atual = anos[3]
  print(credito_atual)
  except IndexError as exc:
raise Exception('Lista de anos é menor que o valor escolhido. ' + \
'Espera-se um valor entre 0 e ' + \
str(len(atual) - 1)
)
except Exception as exc:
raise exc

## funções ## 
import math
print (math.pi)

# programaçã funcional #

emails = [
'andre.perez@gmail.com',
'andre.perez@live.com',
'andre.perez@yahoo.com'
]
provedor_da_google = lambda email: 'gmail in email'
emails_google = filter(provedor_da_google, emails)
print(list(emails_google))

## programação orientada a objeto ## 
def __init__(self, nome="Andre", idade=30, document="123"):
        self.nome = nome
        self.idade = idade

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def getNome(self, document):
        return self.document
      