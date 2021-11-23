# prendiamo un file .csv (comman-separated-values) (simile a .txt)

#se lo apre con qualsiasi altrac cosa diversa da un editor di testo semplice
# --> scarica il .txt

my_file = open('shampoo_sales.txt','r')
#open è una funzione BILT-IN (GIA IN PYTHON)
#(nome file, 'r') sono gli argomenti 
#'r' aprire il file in modalità lettura
#'rw' lettura e scrittura

print(my_file.read()[0:50])
my_file.close()
#consiglio di chiudere sempre il file

#il file mi viene rappresentato come stringa
#[0:50] dalla carattere 0 al 50