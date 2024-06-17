import requests
import re
from bs4 import BeautifulSoup

def buscar_buque():
  url = "https://www.giulianaflores.com.br/tipos-de-flores/d1138/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  auxiliar = soup.find_all("h3", class_="title-item")
  # print(auxiliar[0].text.strip())

  precos = soup.find_all(class_="actual-price")
  # print(precos[0].text.strip())

  busca = input("Digite o nome da flor: ")
  
  print("Buscando buquês... ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘ ⚘\n")
  achou = False
  for (i,flor) in enumerate(auxiliar):
    # print(i,flor.text.strip())
    if busca in flor.text.strip():
      print("\n%s"%flor.text.strip(),end=' - ')
      print(precos[i].text.strip())
      achou = True
  if not achou:
    print("\nNão foi possível encontrar o buquê desejado! =C")
  
  print('\n')
