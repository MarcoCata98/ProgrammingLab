class CSVFile():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "oggetto del file {}".format(self.name)
    
    def get_data(self):
        file = open(self.name)

        for item in file:
            diviso = item.split(",")
            print(diviso)

fail = CSVFile("shampoo_sales.txt")
fail.get_data()

