from projectmodules import bank,cinema
from datetime import datetime
import getpass
import karbar as k

now = datetime.now()
sina = k.User()
k.clear_terminal()
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
        while(True):
            print("1.User")
            print("2.Admin")
            print("3.Back")
            userinput =input("Choose An Option(1-3):")
            if(userinput == "1"):
                user = str(input("Enter your username:   "))
                pwd =getpass.getpass("Enter Your password:   ")
                birthyear =input("Enter The Year of Your Birthday (Example: 2002):   ")
                birthmonth =input("Enter The Month of Your Birthday(Example: (01)):   ")
                birthday =input("Enter The Day of Your Birthday (Example : 06):   ")
                phonenum = input("Enter your phone number(Optional):   ")
                sina.signup(user,pwd,birthday,birthmonth,birthyear,"user",phonenum)
            if(userinput == "2"):
                
                user = str(input("Enter your username:   "))
                pwd =getpass.getpass("Enter Your password:   ")
                birthyear =input("Enter The Year of Your Birthday (Example: 2002):   ")
                birthmonth =input("Enter The Month of Your Birthday(Example: (01)):   ")
                birthday =input("Enter The Day of Your Birthday (Example : 06):   ")
                phonenum = input("Enter your phone number(Optional):   ")
                sina.signup(user,pwd,birthday,birthmonth,birthyear,"admin",phonenum)
            if(userinput == "3"):
                k.clear_terminal()
                break
    if(userinp == "2"):
        k.clear_terminal()
        user = str(input("Enter your username:   "))
        pwd =getpass.getpass("Enter Your password:   ")
        if(sina.checklogin(user,pwd)):
            currentuser = user
            while(True):
                print("1.SeeMyProfile")
                print("2.Edit  Username / Phonenumber")
                print("3.Change Password")
                print("4.MyBanks")
                print("5.Cinema")
                print("6.Back To Main Menu")
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
                        currentuser = userinp
                        bnkinit = bank.bnkinit
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
                                        subscription = bnkinit.getsub(currentuser,selectedbank)
                                        k.clear_terminal()
                                        print(f"\n \n MR/MRS {currentuser} Welcome To Your {selectedbank} Bank Account! You're Using {subscription} Plan!")
                                        print(f"Today : {now.strftime('%Y')} - {now.strftime('%d')} - {now.strftime('%m')}")
                                        print("---------------------")
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
                                                depo = bnkinit.deposit(currentuser,selectedbank,amount,pwd,cvv2)
                                                if(depo[0]):   
                                                    k.clear_terminal()                                                
                                                    print(f"{amount}$ Deposit Succesfully Done!")
                                                    if(depo[1]):    
                                                        print(f"Extra {int(amount) * 0.20}$ Added To Your Wallet For Silver Plan!")
                                                    if(depo[2]):
                                                        print(f"Extra {int(amount) * 0.50}$ Added To Your Wallet For Gold Plan!))")
                                                        print("Take Your Free Energy Drink!")
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
                                            if(bnkmnginp == "5"):
                                                k.clear_terminal()
                                                while(True):
                                                    subscription = bnkinit.getsub(currentuser,selectedbank)
                                                    print(f"Your Current Plan : {subscription} \n")
                                                    if(not subscription == "bronze"):
                                                        if(subscription == "silver"):
                                                            print(f"Plan Remaining Transaction Cashbacks: {bnkinit.remaining(currentuser,selectedbank)}")
                                                        if(subscription == "gold"):
                                                            print(f"Plan Remaining Days: {bnkinit.remaining(currentuser,selectedbank)}")
                                                    print("1.Silver Plan | 10$ ")
                                                    print("2.Gold Plan | 30$")
                                                    print("3.Back")
                                                    bnkmnginp = input("Choose an Option:")
                                                    if(bnkmnginp == "1"):
                                                        pwd = getpass.getpass("Enter Your Bank Password:")
                                                        cvv2 = getpass.getpass("Enter Your Cvv2 Pin :")
                                                        updatesub =bnkinit.update_sub(currentuser,selectedbank,"silver",pwd,cvv2)
                                                        k.clear_terminal()
                                                        print(updatesub)
                                                    if(bnkmnginp == "2"):
                                                        pwd = getpass.getpass("Enter Your Bank Password:")
                                                        cvv2 = getpass.getpass("Enter Your Cvv2 Pin :")
                                                        updatesub =bnkinit.update_sub(currentuser,selectedbank,"gold",pwd,cvv2)
                                                        k.clear_terminal()
                                                        print(updatesub)                                                    
                                                    if(bnkmnginp == "3"):
                                                        k.clear_terminal()
                                                        break
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
                    while(True):
                        print("1.Movie-Show-Times")
                        print("2.Back")
                        userinp4 =input("Choose An Option(1-2)")
                        if(userinp4 == "1"):
                            k.clear_terminal()
                            while(True):
                                cinemaobj =cinema.managecinema()
                                mydict = cinemaobj.showtimelist()
                                userinp5 =input("Choose An Option(1-2):   ")
                                if(not userinp5 == "exit"):
                                    inpint = int(userinp5)
                                    selectedmovie = mydict[inpint]
                                    monthjoined = cinemaobj.apply_discount(currentuser)
                                    if(monthjoined > 1):
                                        cinemaobj.book_seat(selectedmovie,currentuser,monthjoined)
                                    else:
                                        cinemaobj.book_seat(selectedmovie,currentuser)
                                if(userinp5 == "exit"):
                                    k.clear_terminal()
                                    break
                        if(userinp4 == "2"):
                            k.clear_terminal()
                            break
                if(userinp == "6"):
                    k.clear_terminal()
                    break