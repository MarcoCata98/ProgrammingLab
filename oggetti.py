# DEFINIAMO OGGETTO COME GENERICO
# CLASSE E' LA DEFINZIONE GENERICA
# ISTANZA E' UN OGGETTO SPECIFICO

# LE FUNZIONI DENTRO LE CLASSI SI CHIAMANO METODI
# LE VARIABILI DENTRO LE CLASSI SI CHIAMANO ATTRIBUTI

# CLASSE CON INIZIALIZZAZIONE DEGLI ATTRIBUTI
# ==> DIVENTA UN ISTANZA

#LA STESSA CLASSE PUO' ESSERE INSTAZIIATA
#CON DIVERSI ATTRIBUTI CREANDO 2 ISTANZE DIVERSE


# ISTANZA 1
# NOME : MARIO
# ETA : 10

#SE CHIAMO PERSONA 1, ETA ==> 10

# caratteri minuscoli e underscore per le VARIABILI
# CamelCase per il nome delle CLASSI
# __METODOINTERNO__

#---------------------------------
# IN PYTHON TUTTO E' UN OGGETTO
# se vedo cosa ce dentro una stringa -> vedo i METODI
# trovo _add_(unisce le stringhe), startswith(inizia con)
# se hanno gli __x__ -> non servono essere richiamate
#st = "dio"
#print(st.title()) 
#--> .title è un metodo che trovo nell'oggetto stringa


#OPERAZIONI IN-PLACE NON TORNANO UN VALORE
# ES : list.reverse() -> non torna nulla
#OPERAZIONI NON IN-PLACE TORNANO UN VALORE
 # ES : string.split(",") -> torna la lista splittata

 #--------------------------------------------
 # DEFINIRE OGGETTI IN PYTHON
class Person():
    pass #istruzione nulla per avere un blocco vuoto

person = Person()
#print(person) # mi stampa la locazione di memoria

class Animal():
    def __init__(self,name,surname): 
    #istanzio con la funzione __ini__
        self.name = name
        self.surname = surname
    #uso la funzione self --> passata alla funzione
    #per inizializzare degli attributi
    def __str__(self):
    #con __str__ come l oggetto venga rappresentato
        return "animale {} {}".format(self.name, self.surname)
    #se richiamo Animale --> animale nome cognome

animale = Animal('honey','rossi')
#associo ad animale una classe con gli attributi
print(animale)
print(animale.name)
print(animale.surname)