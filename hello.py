print('hello world!')

# commenti


#scrivere subito il nome della variabile
intero = 1
decimale = 1.1
stringa = 'ciao'
boleano = True
vuoto = None

print("valore : {}".format(intero))

#stringhe slicing
print("{}".format(stringa[0:2]));

#liste
my_list = [1,2,3,4]
my_list2 = ['marco','irene','paolo']

#dizionari -> sono liste più evolute
my_dizionario = {'Trieste' : 34170,'Padova': 30103}
#associo a un elemento stringa una chiave numerica
#utile come struttura dati

#funzione per il my_dizionario (molte) esempio:
print("gimme {}".format(my_dizionario['Trieste']))
#posso richiamare la chiave di trieste nel dizionario 


#condizionali e cicli
i=0
while i<10:
  if(boleano==False):
    print("La via del signore è {}".format(decimale))
  elif(stringa=='ciao'):
    print("si ",end="")
  i=i+1
print("\n")

for i in range(10): #range 10 è una lista da [0..9]
  print("{} ".format(i+1),end="" )

print("\n")

#funzioni
def funzione(elemento1,elemento2):
  print("io ho {} e {}".format(elemento1, elemento2))
  
def ritorno(n1,n2):
  return n1+n2

arg1 = 5;
arg2 = 6;

funzione(arg1,arg2)
print("risultato {}".format(ritorno(arg1,arg2)))
#le funzioni lavorano con con le variabili locali
#non usare variabili fuori dalla funzione 
#o passate come argomento

print("\n")

#moduli
#bisogna importarli
import math
math.sqrt(600)
#oppure
from math import sqrt
sqrt(600)

#-------------------
#esercizio

lista = ["marco", "irene", "paolo"]
if "marco" in lista:
  print("marcooooooo")