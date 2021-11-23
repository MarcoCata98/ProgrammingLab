file = open('shampoo_sales.txt', 'r')
soldi = []

for item in file:
    parti = item.split(',')
    #print(parti)
    if parti[0]!= 'Date':
        data = parti[0]
        valori = parti[1]
        #print(valori)
        soldi.append(float(valori))

somma = 0
for i in soldi:
   somma = somma + i

print(somma)