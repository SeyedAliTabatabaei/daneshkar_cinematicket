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
        selectbank = self.bankdata[user].keys()
        i = 0
        bnklist = {}
        for key in selectbank:
            bnklist[i] = key
            i =+ 1
        return bnklist

    def getbalance(self,user,bank):
        pass
    def deposit(self):
        pass
    def withdraw(self):
        pass
    def transfer(self):
        pass

bnkinit = banksystem()