#funzione che somma tutti gli elementi di una lista

lista = [1,2,3,4,5]


def somma(lista):
  somma = 0
  for item in lista:
    somma = somma + item
  return somma

print("{}".format(somma(lista)))