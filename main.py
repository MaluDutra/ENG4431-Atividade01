from os import listxattr
from sopa import buscar_buque
from datetime import datetime
#Definindo Classes
class Flor:
  def __init__(self,id,nome,cor,preco,data,especie):
    self.id = id
    self.nome = nome
    self.cor = cor
    self.preco = preco
    self.data = data
    self.especie = especie

  def adicionar(self):
    arquivo = open("flores.txt", "a")
    arquivo.write("%d,%s,%s,%.2f,%s,%s\n"%(self.id,self.nome,self.cor,self.preco,self.data,self.especie))
    arquivo.close()
    

#Definindo Funções
def menu():
  print("\n✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿\n")
  print("Bem-vindo(a) à Floricultura!\nO que deseja fazer?\n\n")
  print("1 - Adicionar Flor\n2 - Remover Flor\n3 - Atualizar Flor\n4 - Listar Flores\n5 - Acessar Flor\n6 - Buscar preço do buquê\n7 - Sair\n\n")
  print("✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿ ✿\n")


def eh_data(data):
  formato = "%d/%m/%Y"
  try:
    res = bool(datetime.strptime(data, formato))
  except ValueError:
    res = False
  return res


def remover_flor():
  id_removido = False #precisa ser confirmada e id inexistente
  id_remover = input("Digite o ID da flor que deseja remover: ")
  if not id_remover.isdigit():
    print("\nID inválido! Digite um número!\n")
    return
  certeza = input("Tem certeza que deseja remover essa flor (s/n)? ")
  if certeza.upper() == "S":
    print("Removendo Flor... ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘\n")
    for flor in lista:
      if int(flor.id) == int(id_remover):
        cont = 0
        lista.remove(flor)
        id_removido = True
  else:
    print("\nOperação cancelada!\n")
  if id_removido:
    arquivo = open("flores.txt", "w")
    for flor in lista:
      cont+=1
      arquivo.write("%d,%s,%s,%.2f,%s,%s\n"%(cont,flor.nome,flor.cor,flor.preco,flor.data,flor.especie))
    print("\nFlor removida com sucesso!\n")
  else:
    print("Flor não encontrada!\n")


def atualizar_flor():
  id_achado = False
  id_desejado = input("Qual o ID da flor que deseja atualizar? ")
  if not id_desejado.isdigit():
    print("\nID inválido! Digite um número!\n")
    return
  for flor in lista:
    if flor.id == int(id_desejado):
      id_achado = True
      print("Atualizando Flor %s... ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘\n"%flor.nome)
      flor.nome = input("Digite o novo nome da flor: ")
      flor.cor = input("Digite a nova cor da flor: ")
      flor.preco = float(input("Digite o novo preço da flor: "))
      flor.data = input("Digite a nova data de entrada da flor (dd/mm/aaaa): ")
      while not eh_data(flor.data):
        print("\nData inválida! Tente novamente!!\n")
        flor.data = input("Digite a nova data de entrada da flor (dd/mm/aaaa): ")
      flor.especie = input("Digite a nova especie da flor: ")
  if id_achado:
    arquivo = open("flores.txt", "w")
    for flor in lista:
      arquivo.write("%d,%s,%s,%.2f,%s,%s\n"%(flor.id,flor.nome,flor.cor,flor.preco,flor.data,flor.especie))
    arquivo.close()
  else:
    print("\nID inexistente! =C\n")


def acessar_flor():
  id_desejado = input("Qual o ID da flor que deseja acessar? ")
  if not id_desejado.isdigit():
    print("\nID inválido! Digite um número!\n")
    return
  for flor in lista:
    if flor.id == int(id_desejado):
      print("Acessando Flor de Id %d... ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘\n") 
      print("Nome: %s\nCor: %s\nPreço: %.2f\nData de entrada: %s\nEspécie: %s\n"%(flor.nome,flor.cor,flor.preco,flor.data,flor.especie))
      return
  print("\nID inexistente! =C\n")
      

def listar_flores():
  print("Listando Flores... ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘\n")
  for flor in lista:
    print("%d: %s - R$%.2f\n"%(flor.id, flor.nome,flor.preco))
  print("⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘\n")
  
  
#Bloco Principal

parar = True

while parar:
  menu()
  resposta = int(input("Digite uma das opções acima: "))
  print('\n')
  
  global lista
  lista = list()
  arquivo = open("flores.txt", "r")
  global cont
  cont = 0
  for linha in arquivo:
    cont+=1
    valores = linha.split(",")
    florzinha = Flor(int(valores[0].strip()),valores[1].strip(),valores[2].strip(),float(valores[3].strip()),valores[4].strip(),valores[5].strip())
    lista.append(florzinha)
  arquivo.close()
  
  if resposta == 1:
    print("Adicionando Flor... ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘\n")
    cont +=1 
    nome = input("Digite o nome da flor: ")
    cor = input("Digite a cor da flor: ")
    preco = float(input("Digite o preço da flor: "))
    data = input("Digite a data de entrada da flor (dd/mm/aaaa): ")
    while not eh_data(data):
      print("\nData inválida! Tente novamente!!\n")
      data = input("Digite a data de entrada da flor (dd/mm/aaaa): ")
      
    especie = input("Digite a espécie da flor: ")
    flor = Flor(cont,nome,cor,preco,data,especie)
    flor.adicionar()
    
  elif resposta == 2:
    remover_flor()
  
  elif resposta == 3:
    atualizar_flor() 
    
  elif resposta == 4:
    listar_flores()
    
  elif resposta == 5:
    acessar_flor() 
    
  elif resposta == 6:
    buscar_buque()
    
  elif resposta == 7:
    parar = False 
  else:
    print("Opção inválida! Tente novamente.\n")
    