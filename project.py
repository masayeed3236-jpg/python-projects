# CREATING PYTHON PROJECT FOR EXPENSE TRACKER 

spending = []     #list of all expenses in form of dictionary
print("welcome to the EXPENCE TRACKER APP ")

while True:
    print("======MENU=====")
    print("1. add your expenses ")
    print("2. view all your expenses ")
    print("3. make total of your expenses ")
    print("4. exit ")

    choice = int(input("enter your choice :)  "))

#adding the expenses

    if (choice == 1):
        date = input("enter the date like(day month) ")
        category = input("enter the category like(clothes,food,travel,entertainment) ")
        details = input("enter some more details ")
        amount = int(input("enter the amount spent  "))

        spend = {
            "date": date,
            "category": category,
            "details": details,
            "amount": amount
        }

        spending.append(spend)
        print(" \n expenses added succesfully  ")

#viewing the expenses by choice 2 

    elif(choice == 2):
        if (len(spending) == 0):
            print("first spend the money  ")
        else :
            print("this is your spending  ")
            count = 1
            for pen in spending :
                print(f"spending number {count} -->  {pen["date"]},{pen["category"]},{pen["details"]},{pen["amount"]} ")
                count = count+1

#viewing total spending
    elif (choice == 3):
        total = 0
        for pen in spending:
            total = total + pen["amount"]

        print(f" \n total spending = {total}")


#exit
    elif(choice == 4):
        print(" thanks for using our system ")
        break


    else :
        print("INVALID CHOICE -  enter the numbers between 1 to 4 : ")
        

