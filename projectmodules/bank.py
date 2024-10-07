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

        print(self.bankdata)
        return self.bankdata

    def getbalance(self):
        pass
    def deposit(self):
        pass
    def withdraw(self):
        pass
    def transfer(self):
        pass

bnkinit = banksystem()