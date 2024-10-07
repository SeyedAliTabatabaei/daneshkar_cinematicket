from datetime import datetime 
import json
import logging
import os
now = datetime.now()  
logging.basicConfig(
    filename='cinematicket.log',  
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')
class User:
    def __init__(self,username,password,birthdate,regdate,phone_number):
        self.username = username
        self.password = password
        self.birthdate = birthdate
        self.regdate = regdate
        self.phone_number = phone_number
        self.users = usersdict = {}
        
        with open('data.json', 'r') as f:
            try:
                data = json.load(f)
                if(data):
                    self.users= data
            except json.JSONDecodeError:
                pass     
        usercount = 0
    def checklogin(self,username,password):
        if(len(self.users) > 0):
            if(username in self.users):
                if(username == self.users[username]["username"]) and (password == self.users[username]["password"]):

                    clear_terminal()
                    with open('data.json', 'r') as f:
                        try:
                            data = json.load(f)
                            userdata = data[username]
                            if(userdata):
                                self.username = userdata['username']
                                self.password = userdata['password']
                                self.birthdate = userdata['birthdate']
                                self.regdate = userdata['regdate']
                                self.phone_number = userdata['phone_number']
                        except json.JSONDecodeError:
                            pass   
                    logging.info(f'user logged in successfully{self.users}')
                    print("\n\n\n  You've Logged in successfully! \n\n\n ")
                    return True
                else:
                    clear_terminal()
                    print("\n\n\n Wrong user or password! \n\n\n ")
        else:
            clear_terminal()
            
            print("\n\n\n    Please SignUp First!      \n\n\n")
    def signup(self,username,password,birthdate,phone_number=None):
        self.username = username
        self.password = password
        self.birthdate = birthdate
        self.regdate = str(now)
        self.phone_number = phone_number
                                        #چک کردن تکراری نبودن نام کاربری
        if(username in self.users):
            clear_terminal()
            logging.info(f'invalid username entered')
            print("\n\n\n  Your username is Already Taken! \n\n\n ")
        else:
                                        #چک کردن طول رمزعبور
            if(len(self.password) >= 4):

                self.users[username] = {
                    'id':len(self.users),
                    'username':username,
                    'password':password,
                    'birthdate':birthdate,
                    'regdate':str(now),
                    'phone_number':phone_number,
                }
            with open('data.json', 'w') as f:
                json.dump(self.users, f)
            clear_terminal()
            logging.info(f'SignedUp Successfully!{self.users}')
            print("\n\n\n  You've been signed up successfully! \n\n\n ")
    def updateusername(self,newuser):
        user = self.username
        self.users[user].pop("username")
        self.users[user]["username"] = newuser
        self.users[newuser]= self.users[user]
        self.users.pop(user)
        self.username = newuser
        with open('data.json', 'w') as f:
            json.dump(self.users, f)
        clear_terminal()
        logging.info(f'Username Updated!{self.users}')
        print("Username Update Successfully Done!")

    def updatephonenumber(self,newphone):
        name =self.username
        self.users[name].pop("phone_number")
        self.users[name]["phone_number"] = newphone
        self.phone_number = newphone
        with open('data.json', 'w') as f:
            json.dump(self.users, f)
        clear_terminal()   
        logging.info(f'Phone Number Updated!{self.users}')    
        print("Phone Number Update Successfully Done!")
    def changepass(self,old,new):
        name =self.username
        print(name)
        if(self.users[name]['password'] == old):
            self.users[name].pop("password")
            self.users[name]["password"] = new
            self.password = new
            with open('data.json', 'w') as f:
               json.dump(self.users, f)
            return True
        
        else:
            clear_terminal()
            print("Your password is Wrong")
    def __str__(self):
        return f"UserName : {self.username} PhoneNumber : {self.phone_number} Birthdate : {self.birthdate} Registered Date : {self.regdate}"
