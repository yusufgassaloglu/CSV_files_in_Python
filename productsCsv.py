from csv import DictReader
from csv import DictWriter
from csv import reader
from csv import writer

def create():
     print("If a file with the same name already exists in the same directory, the old file is deleted.")
     print("New file will be created in the same directory as this file.")
     file_name = input("File name: ")
     with open(file_name+".csv","w") as file:
               headers = ["Name", "Price", "Release Date", "Type"]
               writer = DictWriter(file, headers)
               writer.writeheader()
     print(file_name + " created")
     file.close()

def add():
     while True:
          try:
               file_name = input("File name: ")
               reader(open(file_name+".csv"))
               break
          except:
               print(f"{file_name} does not exist")
     while True:
          _how_many = input("How many values to add: ").rstrip().lstrip()
          if _how_many.isdigit() == 1:
               how_many = int(_how_many)
               if how_many > 0:
                    break
               else:
                    print("ERROR")
          else:
               print("ERROR")
     count = how_many
     while how_many > 0:
          with open(file_name+".csv","a") as file:                    
               headers = ["Name", "Price", "Release Date", "Type"]
               writer = DictWriter(file, headers)
               name = input("Name: ")
               price = input("Price: ")
               relase_date = input("Release date: ")
               _type = input("Type: ")
               writer.writerow({
                    "Name" : name,
                    "Price" : price,
                    "Release Date" : relase_date,
                    "Type" : _type})
               print("*")
               how_many += -1
     if count == 1:
          print(f"{count} value added")
     else:
          print(f"{count} values added")
     file.close()

def change():
     while True:
          try:
               file_name = input("File name: ")
               r = reader(open(file_name+".csv"))
               break
          except:
               print(f"{file_name} does not exist")
     products = list(r)
     for x in products:
          if x == []:
               products.remove(x) 
          else:
               products.append(x)
     lastProducts = [] 
     for i in products: 
          if i not in lastProducts: 
               lastProducts.append(i)
     while True:
          _line = input("Value line: ")         
          if _line.isdigit() == 1:
               line = int(_line)
               if line > 0 :
                    if line <= len(lastProducts)-1:
                         break
                    else:
                         print(f"{_line}. line does not exist.")
               else:
                    print("ERROR")
          else:
               print("ERROR")
     new_name = input("New name: ")
     new_price = input("New price: ")
     new_release = input("New release date: ")
     new_type = input("New type: ") 
     products[line][0] = new_name
     products[line][1] = new_price
     products[line][2] = new_release
     products[line][3] = new_type
     w = writer(open(file_name+".csv", "w"))
     w.writerows(lastProducts)

def delete():
     while True:
          try:
               file_name = input("File name: ")
               reader(open(file_name+".csv"))
               break
          except:
               print(f"{file_name} does not exist")
     r = reader(open(file_name+".csv"))
     products = list(r)
     for x in products:
          if x == []:
               products.remove(x) 
          else:
               products.append(x)
     lastProducts = [] 
     for i in products: 
          if i not in lastProducts: 
               lastProducts.append(i)
     while True:
          _line = input("Value line: ")         
          if _line.isdigit() == 1:
               line = int(_line)
               if line > 0 :
                    if line <= len(lastProducts)-1:
                         break
                    else:
                         print(f"{_line}. line does not exist.")
               else:
                    print("ERROR")
          else:
               print("ERROR") 
     new_name = ""
     new_price = ""
     new_release = ""
     new_type = "" 
     products[line][0] = new_name
     products[line][1] = new_price
     products[line][2] = new_release
     products[line][3] = new_type
     deletedProducts = []
     for j in lastProducts:
          if j != ['', '', '', '']:
               deletedProducts.append(j)
               w = writer(open(file_name+".csv", "w"))
               w.writerows(deletedProducts)

def read():
     print("The file must be in the same directory as this python file.")
     while True:
          try:
               file_name = input("File name: ")
               reader(open(file_name+".csv"))
               break
          except:
               print(f"{file_name} does not exist")
     with open(file_name+".csv") as file:
          products = DictReader(file)
          products = list(products)
          for line,product in enumerate(products):
               print(line+1,"Name:"+product["Name"]+" Price:"+product["Price"]+" Release Date:"+product["Release Date"]+" Type:"+product["Type"])     
     file.close()

while True:
     print('''***
1-Read
2-Create a file
3-Delete
4-Update
5-Exit
***''')
     action = input("Choose action (1,2,3,4,5): ").rstrip().lstrip()

     if action == "1":
          print("1-Read | Enter any value to go to the main menu except 1.")
          readAction = input("Choose action: ").rstrip().lstrip()
          if readAction == "1":
               read()
     elif action == "2":
          print("1-Create | Enter any value to go to the main menu except 1.")
          createAction = input("Choose action: ").rstrip().lstrip()
          if createAction == "1":
               create()
     elif action == "3":
          print("1-Delete | Enter any value to go to the main menu except 1.")
          deleteAction = input("Choose action: ").rstrip().lstrip()
          if deleteAction == "1":
               delete()
     elif action == "4":
          print("1-Add 2-Change | Enter any value to go to the main menu except 1 and 2.")
          updateAction = input("Choose action (1,2): ").rstrip().lstrip()
          if updateAction == "1":
               add()
          elif updateAction == "2":
               change()
     elif action == "5":
          break
     else:
          print("!!")
          print("ERROR: Only choose 1,2,3,4,5.")
          print("!!")

     


     