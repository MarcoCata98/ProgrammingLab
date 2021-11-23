my_file = open('shampoo_sales.txt','r')
my_file_contents = my_file.read()

if len(my_file_contents) > 50:
    print(my_file_contents[0:50]+'...')
else:
   print(my_file_contents)


#print(my_file.readline())
#stampa riga per riga

my_file.close()