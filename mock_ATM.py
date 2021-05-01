userName = input("Please enter your name \n")
userNamesDirectory = ['Cyndie', 'Moti', 'Jony', 'Fay']
userNamesPasswords = ['cyn@123', 'motijohnson', 'JO5694', '1985Fay']
userNamesAccountBalance = ['3500ksh', '14,420ksh', '20,536ksh', '5050ksh']
accountId = userNamesDirectory.index(userName)
userId = userNamesDirectory.index(userName)

#-------------Program to authentify username and password------------#

if(userName in userNamesDirectory):
    print("Welcome " + " " + userName)
    password = input("Please enter your Password \n")
 
    if(password == userNamesPasswords[userId]):
        print(userName + ", " + "You are now logged in. ")
        print("Tuesday, April 6, 2021.")
        print("Type '1' for withdrawal. ")
        print("Type '2' for cash deposit. ")
        print("Type '3' for complaint. ")
        print("Type '4' to log out. ")

        selectedOption = int(input("Please type an option here. Eg, '1' . \n"))

        if(selectedOption == 1):
            print("Please type amount you wish to withdraw. \n")
            if(selectedOption != userNamesAccountBalance[accountId]):
                print("Error: Account balance less than amount to withdraw. Please try again. ")
                print("Please type amount you wish to withdraw. \n")
            else:
                print(" take your cash. ")


        if(selectedOption == 2):
            cashDeposit = int(input("How much would you like to deposit? \n"))
           
            print( cashDeposit + userNamesAccountBalance[accountId])


        if(selectedOption == 3):
            complaint = input("What issue would you like to report? \n")  
            print("Thank you for contacting us")

#------program when username and password is incorrect------------#                        
    else:
        print("Password is incorrect. Kindly try again. ")
        password = input("Please enter your Password \n")
else:
    print("UserName not recognized. Please re-enter your UserName again. ")
    userName = input("Please enter your name \n")