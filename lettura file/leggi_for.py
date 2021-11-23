my_file = open('shampoo_sales.txt', 'r')

#python riconosce l'unita base del .txt 
#le righe e non i caratteri
i=0
for item in my_file: 
    if(i < 3):
        print(item)
        i=i+1
      

#posso scrivere anche line al posto di item

my_file.close()

#uso un valore i per leggere un tot di righe
