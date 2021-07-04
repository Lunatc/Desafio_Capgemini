from datetime import datetime
import struct

def search(lista, nome):
    for i in range(len(lista)):
        if list[i] == nome:
            return i
    return -1

def new():
  nome = input('Nome do anúncio:')
  cliente = input('Escreva o nome do cliente:')
  
  dia = input('Dia de início do anúncio:')
  mes = input('Mês de início do anúncio:')
  ano = input('Ano de início do anúncio:')
  
  inicio = (ano + "-" + mes)
  inicio = (inicio + "-" + dia)
  print(inicio)
  inicio = datetime.strptime(inicio, "%ano-%mes-%dia")
  
  dia = input('Dia de fim do anúncio:')
  mes = input('Mês de fim do anúncio:')
  ano = input('Ano de fim do anúncio:')
  
  fim = (ano,'-',+mes,'-'+dia)
  fim = datetime.strptime(ano,mes,dia)
      
  #Calcula quantos dias de anuncio
  dias = abs((fim-inicio).days)  
  investimento = float(input("Investimento por dia:"))

  anuncio = struct.pack(nome,cliente,inicio, fim, investimento, dias)

  list.append(anuncio)
  
  print('Anúncio cadastrado com sucesso');

  

def registro():
  print =('Digite o nome do anúncio a ser buscado:')
  nome = input('Digite o nome do anúncio a ser buscado:')

  anuncio = search(lista, nome)

  if anuncio < 0 : 
    print('Erro, nome não encontrado')
  else:
    print('Valor Total investido:', lista[anuncio[5]])




def menu():

  print('Qual ação deseja realizar?:')
  print('1-Criar novo anúncio')
  print('2-Relatório de um anúncio')

  while 1:
    chosen = False
    while not chosen:
      choice = input()
      if choice not in '012':
        print('Erro, insira novamente:')
      else:
        chosen = True
        if choice =='0':
          break
        if choice == '1':
          new()
        if choice == '2':
          registro()


lista = []
menu()




