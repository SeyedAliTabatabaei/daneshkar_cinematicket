import json
class banksystem:
    def __init__(self):
        self.bankdata = {}
    def create_account(self,user,firstbalance,bankname,pwd,cvv2):
        self.user = user
        self.firstbalance = firstbalance
        self.bankname = bankname
        self.pwd = pwd
        self.cvv2 = cvv2
        databnk = {
            'bank':bankname,
            'balance':firstbalance,
            'password':pwd,
            'cvv2':cvv2,
        }
        if(user in self.bankdata):
            self.bankdata[user][bankname] = databnk
            with open('bankdata.json','w') as file:
                json.dump(self.bankdata,file)
        else:
            self.bankdata[user] = {
                bankname:databnk,
            }
            with open('bankdata.json','w') as file:
                json.dump(self.bankdata,file)

            return self.bankdata
    def accountlist(self,user):
        try:
            with open('bankdata.json','r') as file:
               self.bankdata= json.load(file)
        except:
            pass
        if(user in self.bankdata):
                selectbank = self.bankdata[user].keys()
                i = 0
                bnklist = []
                for key in selectbank:
                    bnklist.append(key)
                return bnklist
        return False

    def getbalance(self,user,bank,pwd,cvv2):
        selectedbank = self.bankdata[user][bank]
        bankpass = selectedbank['password']
        bankcvv2 = selectedbank['cvv2']
        if(bankpass == pwd and bankcvv2 == cvv2):
            balance = self.bankdata[user][bank]['balance']
            print(f"Your Current Balance : {balance}$")
        else:
            print("Invalid Credentials!")
        
    def deposit(self,user,bank,amount,pwd,cvv2):
        selectedbank = self.bankdata[user][bank]
        bankpass = selectedbank['password']
        bankcvv2 = selectedbank['cvv2']
        if(bankpass == pwd and bankcvv2 == cvv2):
            balancestr = self.bankdata[user][bank]['balance']
            balanceint = int(balancestr) + int(amount) 
            self.bankdata[user][bank]['balance'] = str(balanceint)
            with open('bankdata.json','w') as file:
                json.dump(self.bankdata,file)  
            return True
        else:
            print("Invalid Credentials!")
    def withdraw(self):
        pass
    def transfer(self):
        pass

bnkinit = banksystem()