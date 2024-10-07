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
            while(True):
                print("1.SeeMyProfile")
                print("2.Edit  Username / Phonenumber")
                print("3.Change Password")
                print("4.Back To Main Menu")
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
                if(userinp == "4"):
                    k.clear_terminal()
                    break