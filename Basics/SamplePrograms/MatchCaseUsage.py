#In Other Languages this is called Switch case (Came to python 3.10 onwards)

Grade = input("Enter the Grade: ").upper() #Converting the input to uppercase

match Grade:
    case "A":
        print("The Grade is : ",Grade)
    case "B":
        print("The Grade is : ",Grade)

    case "C":
        print("The Grade is : ",Grade)

    case "D":
        print("The Grade is : ",Grade)

    case "E":
        print("The Grade is : ",Grade)

    case _:
        print("Invalid Grade given: ",Grade)

