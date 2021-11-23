# / DIVIDENDO 2 INTERI OTTERREMO UN FLOAT
# // DIVIDERE 2 INTERI COSI OTTERRAI UN INTERO 10//3 = 3

# "script \" backslash per i caratteri speciali
# \n per a capo - \t per tabbare
# ("""cosi lo script segue gli a capo nello script""")
# "a" + "b" = ab     ---     24 * "hi" = 42 volte hi

#  x = input("come ti chiami : ")    print("il mio nome è " + x)
#INPUT() PRENDE SOLO STRINGHE , E VANNO CONVERTITE IN INT

#conversione di variabili  int(input()) o str(21) o float()
#es :
#a = "7"
#a = a + "0"
#print(a)
#a = int(a)
#print(a+2)
#a = str(a) + "b"
#print(a)

# BOOLEANI  print(4==5) out:False -> Print(4==4) out:True
# if qualcosa : 
#   statement se vero
#elif = else if (qualcosa) :
# and not or --> si scrivono cosi

# while loops
#es:
#x = 1
#while x<=10 :
#    if x%2==0 :
#        print(str(x) + " è pari")
#    else:
#        print(str(x) + " è dispari")
#    x = x+1
# non si possono sommare int con stringhe quindi converto
# posso usare il BREAK per interrompere il while
# CONTINUE mi fa ripartire dall'inizio del loop saltando
#es:
#w = int(input("peso "))
#h = float(input("altezza "))
#b = w/(h**2)
#if b<18.5:
#    print("Underweight")
#elif b>=18.5 and b<25 :
#    print("Normal")
#elif b>=25 and b<30 :
#    print("Overweight")
#elif b>=30:
#    print("Obesity")


#LISTE = ARRAY
#POSSO FARE ANCHE MATRICI 
# a = [
#    [1,2,3]
#    [3,6,3]
#]
# print a[2][1] secondo item prima riga (parte da 0)
# SI POSSONO PRINTARE GLI ARRAY --> print(a)

# STRINGE COME MATRICI
# a = "bella ciao"
# print(a[6])--> il sesto carattere = c

#a = [1,2,3]   #b = [4,5,6]
# unire 2 liste print(a+b) --> 1,2,3,4,5,6

# OPERATORI NELLE LISTE

# in 
#se ELEMENTO in LISTA = True  (se c'è)
#es:
#words = ["spam", "egg", "spam", "sausage"]
#print("spam" in words)

#  not in
# se  ELEMENTO not in LISTA = True  (se non c'è)
#es :
#words = ["spam", "egg", "spam", "sausage"]
#print("sperma" not in words)
#oppure  not ELEMENTO in LISTA 
#print (not "sperma" in words)


# FOR LOOP --> for i in lista:

# ricerca da t in uno script

#stringa = "altezza volante del tetto di tettonia"
#t = 0
#for i in stringa:
#    if (i == "t"):
#        t = t+1
#print(t)

#ricordo che le stringhe sono delle liste


# RANGE() è una funzione
# range(10) è una una serie di numeri che va da 0,1,...,9 (10-1)
# LIST() è una funzione
# list(1,2,3,4) trasforma una serie di elementi in una lista

# ==> list(range(10)) --> Trasforma in una lista i numeri da 0-9
#es:
# nums = list(range(5))
# print(nums[4])
# --> nums = [0,1,2,3,4]

# RANGE(DA x A y-1) 
#--> range(3,8) = una serie di numeri da 3,..,7  (8-1)
# range(20) == range(0,20)

#RANGE(DA x A y-1 SALTANDO z PASSI ALLA VOLTA)
#--> range(5 20 2) = 5,7,9,11,13,15,17,19 

#INTEGRANDO RANGE A FOR
# for i in range(10) --> non serve metterlo in list() è sottointeso

#for i in range(0,10,2):
#    print (i)

#--------------------------------
# LIST SLICE 
# array[a:b] --> come in range va da l'elemento a al (b-1)
#lettere = ["a","b","c","d","e","f","g"]
#a = lettere[2:6] 
#print(a) --> c d e f
#print(lettere[0:1]) --> "a" e basta

# se faccio lettere[:6] --> OMETTO IL PRIMO ELEMENTO 
# allora parte da 0 della lista fino a (6-1)
#se OMETTO IL SECONDO [3:] VA FINO IN FONDO --> ULTIMO COMPRESO

# come nel RANGE 
# [a : b : c] --> vado da A a (B-1) prendendo un numero ogni C numeri
#print(lettere[::2]) -->. a , c, e ,g 
#quindi prendo a e dal prossimo conto 1->b , 2->c = prendo 2
#SE NON METTO IL NUMERO DI INIZIO E FINE --> va dall'inizio alla fine

