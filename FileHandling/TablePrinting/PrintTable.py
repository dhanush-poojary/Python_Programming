#Stores table of Each number upto n in different files
n = int(input("Enter the number till where you want table:  "))

for k in range(1,n+1):
    table = ""
    for i in range(1,11):
      table += f"{k} X {i} = {k*i}\n"
    with open(f"FileHandling/TablePrinting/table_{k}.txt","w") as f: #Creates a new file for storing table of k
       f.write(table)
else:
   print("All Table Files Generated !!!")
