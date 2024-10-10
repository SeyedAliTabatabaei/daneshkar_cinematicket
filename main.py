from projectmodules import bank
import getpass
import karbar as k

sina = k.User("sina","sina123","1381/28/06","","")
def print_menu():

    print("0.Exit")
    print("1.SignUp")
    print("2.Login")

while(True):
    print_menu()
    userinp = input("Choose An Option :   ")
    if(userinp == "0"):
  
        break

    if(userinp == "1"):
        user = str(input("Enter your username:   "))
        pwd =getpass.getpass("Enter Your password:   ")
        birthdate =input("Enter Your Birthdate:   ")
        phonenum = input("Enter your phone number(Optional):   ")
        sina.signup(user,pwd,birthdate,phonenum)
    if(userinp == "2"):
        user = str(input("Enter your username:   "))
        pwd =getpass.getpass("Enter Your password:   ")
        if(sina.checklogin(user,pwd)):
            currentuser = user
            while(True):
                print("1.SeeMyProfile")
                print("2.Edit  Username / Phonenumber")
                print("3.Change Password")
                print("4.MyBank")
                print("5.Back To Main Menu")
                userinp = input(" \n Choose An option:")
                if(userinp == "1"):
                    k.clear_terminal()
                    print(sina)
                if(userinp == "2"):
                    k.clear_terminal()
                    print("1.Edit Username")
                    print("2.Edit Phonenumber")
                    userinp = input(" \n Choose An option:")
                    if(userinp == "1"):
                        userinp = input('Enter Your new Username')
                        sina.updateusername(userinp)
                    if(userinp =="2"):
                        userinp = input('Enter Your New phone number')
                        sina.updatephonenumber(userinp)
                if(userinp == "3"):
                    userinp = getpass.getpass('Enter Your Current Password: ')
                    userinp2 = getpass.getpass("Enter Your New Password:")
                    userinp3 = getpass.getpass("Repeat Your New Password:")
                    if(userinp2 == userinp3):
                        if(sina.changepass(userinp,userinp2)):
                            k.clear_terminal()
                            print("Password Changed Successfully!")
                    else:
                        k.clear_terminal()
                        print("Your New Password and Repeat is Not the Same")
                if(userinp =="4"):
                    while True:
                        bnkinit =bank.bnkinit
                
                        print("1.Create Account")
                        print("2.MyAccounts")
                        print("3.Back")
                        usrbankinp = input("Choose One Option:")
                        if(usrbankinp == "1"):
                            print("1.Saman")
                            print("2.Melli")
                            print("3.Sepah")
                            bankselect = {
                                '1':'saman',
                                '2':'melli',
                                '3':'sepah',
                            }
                            bankinp =input("Choose The Bank You Want to Create Account:")
                            if(bankinp in bankselect):
                                bankname = bankselect[bankinp]

                            firstbalance =input("First deposit Amount(At least 10$):")
                            pswd =input("Enter your Bank Account Password:")
                            cvv2 = input("Enter Your Cvv2 Pin:")
                            createacc = bnkinit.create_account(currentuser,firstbalance,bankname,pswd,cvv2)
                            if(createacc):
                                k.clear_terminal()
                                print("Your Bank Account has been opened SuccessFully!")
                        if(usrbankinp == "2"):
                            k.clear_terminal()
                            listbank = bnkinit.accountlist(currentuser)
                            if(listbank):
                                while(True):
                                    counter = 0
                                    for i in listbank:
                                        print(f"{counter}.{i}")
                                        counter += 1
                                    print(f"{len(listbank)}.back")
                                    selectedbank = input("Choose An Option:")
                                    if(int(selectedbank) == len(listbank)):
                                        k.clear_terminal()
                                        break
                                    else:
                                        selectedbank = int(selectedbank)
                                        selectedbank = listbank[selectedbank]
                                        
                                        k.clear_terminal()
                                        print(f" MR/MRS {currentuser} Welcome To Your {selectedbank} Bank Account! \n ")
                                        while(True):
                                            print("1.Balance")
                                            print("2.Deposit")
                                            print("3.Withdraw")
                                            print("4.Transfer Money")
                                            print("5.Upgrade Your Subscription")
                                            print("6.Back")
                                            bnkmnginp = input("Choose an Option:")
                                            if(bnkmnginp == "1"):
                                                k.clear_terminal()
                                                pwd = getpass.getpass("Enter Your Bank Password:")
                                                cvv2 = getpass.getpass("Enter Your Cvv2 Pin :")
                                                bnkinit.getbalance(currentuser,selectedbank,pwd,cvv2)
                                            if(bnkmnginp == "2"):
                                                k.clear_terminal()
                                                pwd = getpass.getpass("Enter Your Bank Password:")
                                                cvv2 = getpass.getpass("Enter Your Cvv2 Pin :")
                                                amount = input("Enter Amount You Want to Deposit:")
                                                if(bnkinit.deposit(currentuser,selectedbank,amount,pwd,cvv2)):
                                                    print("Deposit Succesfully Done!")
                                            if(bnkmnginp == "3"):
                                                k.clear_terminal()
                                                pwd = getpass.getpass("Enter Your Bank Password:")
                                                cvv2 = getpass.getpass("Enter Your Cvv2 Pin :")
                                                amount = input("Enter Amount You Want to Withdraw:")
                                                if(bnkinit.withdraw(currentuser,selectedbank,amount,pwd,cvv2)):
                                                    print("Withdraw Succesfully Done!")
                                            if(bnkmnginp == "4"):
                                                k.clear_terminal()
                                                cnt= 0
                                                bnklist = bnkinit.transferablebanks(currentuser,selectedbank)
                                                for bnk in bnklist:
                                                    print(f"{cnt}.{bnk}")
                                                    cnt += 1
                                                targetbank = int(input("Choose an Option:"))
                                                targetbank = bnklist[targetbank]
                                                pwd = getpass.getpass("Enter Your Bank Password:")
                                                cvv2 = getpass.getpass("Enter Your Cvv2 Pin :")
                                                amount = input("Enter Amount You Want to Withdraw:")
                                                
                                                if(bnkinit.transfer(currentuser,selectedbank,targetbank,amount,pwd,cvv2)):
                                                    k.clear_terminal()
                                                    print("Transfer Succesfully Done!")
                                            if(bnkmnginp == "6"):
                                                k.clear_terminal()
                                                break

                            else:
                                k.clear_terminal()
                                print("Please Create an Account First! \n")
                        if(usrbankinp == "3"):
                            k.clear_terminal()
                            break

                              
                if(userinp == "5"):
                    k.clear_terminal()
                    break