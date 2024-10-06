import os
import getpass
def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
class User:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.users = usersdict = {}
        usercount = 0
    def checklogin(self,username,password):
        if(len(self.users) > 0):
            if(username in self.users):
                if(username == self.users[username]["username"]) and (password == self.users[username]["password"]):
                    clear_terminal()
                    print("\n\n\n  You've Logged in successfully! \n\n\n ")
                    return True
                else:
                    clear_terminal()
                    print("\n\n\n Wrong user or password! \n\n\n ")
        else:
            clear_terminal()
            print("\n\n\n    Please SignUp First!      \n\n\n")
    def signup(self,username,password,phone_number=None):
        self.username = username
        self.password = password
        self.phone_number = phone_number
                                        #چک کردن تکراری نبودن نام کاربری
        if(username in self.users):
            clear_terminal()
            print("\n\n\n  Your username is Already Taken! \n\n\n ")
        else:
                                        #چک کردن طول رمزعبور
            if(len(self.password) >= 4):

                self.users[username] = {
                    'id':len(self.users),
                    'username':username,
                    'password':password,
                    'phone_number':phone_number,
                }
            clear_terminal()
            print("\n\n\n  You've been signed up successfully! \n\n\n ")
    def updateusername(self,newuser):
        user = self.username
        self.users[user].pop("username")
        self.users[user]["username"] = newuser
        self.users[newuser]= self.users[user]
        self.users.pop(user)
        self.username = newuser
        clear_terminal()
        print("Successfully Done!")

    def updatephonenumber(self,newphone):
        name =self.username
        self.users[name].pop("phone_number")
        self.users[name]["phone_number"] = newphone
        self.phone_number = newphone
        clear_terminal()       
        print("Successfully Done!")
    def changepass(self,old,new):
        name =self.username
        if(self.users[name]['password'] == old):
            self.users[name].pop("password")
            self.users[name]["password"] = new
            self.password = new
            clear_terminal()
        else:
            clear_terminal()
            print("Your password is Wrong")
    def __str__(self):
        return f"UserName : {self.username} PhoneNumber : {self.phone_number}"

sina = User("sinatbtb","Arman12A")
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
        phonenum = input("Enter your phone number:   ")
        sina.signup(user,pwd,phonenum)
    if(userinp == "2"):
        user = str(input("Enter your username:   "))
        pwd =getpass.getpass("Enter Your password:   ")
        if(sina.checklogin(user,pwd)):
           
            print("1.SeeMyProfile")
            print("2.Edit  Username / Phonenumber")
            print("3.Change Password")
            print("4.Back To Main Menu")
            userinp = input(" \n Choose An option:")
            if(userinp == "1"):
                clear_terminal()
                print(sina)
            if(userinp == "2"):
                clear_terminal()
                print("1.Edit Username")
                print("2.Edit Phonenumber")
                userinp = input(" \n Choose An option:")
                if(userinp == "1"):
                    userinp = input('Enter Your new Username')
                    sina.updateusername(userinp,)
                if(userinp =="2"):
                    userinp = input('Enter Your New phone number')
                    sina.updatephonenumber(userinp)
            if(userinp == "3"):
                userinp = getpass.getpass('Enter Your Current Password: ')
                userinp2 = getpass.getpass("Enter Your New Password:")
                userinp3 = getpass.getpass("Repeat Your New Password:")
                if(userinp2 == userinp3):
                    sina.changepass(userinp,userinp2)
                else:
                    clear_terminal()
                    print("Your New Password and Repeat is Not the Same")
            if(userinp == "4"):
              clear_terminal()