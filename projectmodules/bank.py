from datetime import datetime, timedelta
import json
class banksystem:
    def __init__(self):
        self.bankdata = {}
    def create_account(self,user,firstbalance,bankname,pwd,cvv2,subscription='bronze'):
        self.user = user
        self.firstbalance = firstbalance
        self.bankname = bankname
        self.pwd = pwd
        self.cvv2 = cvv2
        self.subscription = subscription
        databnk = {
            'bank':bankname,
            'balance':firstbalance,
            'password':pwd,
            'cvv2':cvv2,
            'subscription':subscription
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
    def getsub(self,user,bank):
        selectedbank = self.bankdata[user][bank]   
        plan = selectedbank['subscription']
        return plan
    def remaining(self,user,bank):
        selectedbank = self.bankdata[user][bank]   
        plan = selectedbank['subscription']
        if(plan == "silver"):
            remaining = selectedbank['silver_cashback_remaining']
        if(plan == "gold"):
            remaining = selectedbank['gold_cashback_end_date']
            remaining = datetime.fromisoformat(remaining)
            remaining  = (remaining - datetime.now()).days
        return remaining
    def update_sub(self,user,bank,subtype,pwd,cvv2):
        result = "There Was a Problem Updating Your plan"
        selectedbank = self.bankdata[user][bank]
        bankpass = selectedbank['password']
        bankcvv2 = selectedbank['cvv2']
        if(bankpass == pwd and bankcvv2 == cvv2): 
            subscription = selectedbank['subscription']
            change_sub = False
            if(subtype =="silver"):
                if(subscription =="bronze"):
                    subscription = "silver"
                    amount = 10
                    change_sub = True
                else:
                    result = f"You Are using {subscription} plan already!"
            if(subtype =="gold"):
                if(subscription == "bronze" or subscription == "silver"):
                    subscription = "gold"
                    amount =30
                    change_sub = True
                else:
                   result = f"You Are using {subscription} plan already!"
            balancestr = self.bankdata[user][bank]['balance']
            selectedbank['subscription'] = subscription
            if(subscription == "silver"):
                selectedbank['silver_cashback_remaining'] = 3
            if(subscription == "gold"):
                current_time = datetime.now()
                one_month_later = current_time + timedelta(days=30)
                selectedbank['gold_cashback_end_date'] = (one_month_later.isoformat())
            if(change_sub):
                if(int(balancestr) > int(amount)):
                    balanceint = int(balancestr) - int(amount) 
                    self.bankdata[user][bank]['balance'] = str(balanceint)
                    result = f"Your Subscription Updated to {subtype}!"
                    with open('bankdata.json','w') as file:
                        json.dump(self.bankdata,file) 
                else:
                    result = "Your Balance is Not Enough!"
        else:
            result = "Invalid Credentials!"
        return result 


      

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
    def withdraw(self,user,bank,amount,pwd,cvv2):
        selectedbank = self.bankdata[user][bank]
        bankpass = selectedbank['password']
        bankcvv2 = selectedbank['cvv2']
        if(bankpass == pwd and bankcvv2 == cvv2):
            balancestr = self.bankdata[user][bank]['balance']
            if(int(balancestr) > int(amount)):
                balanceint = int(balancestr) - int(amount) 
                self.bankdata[user][bank]['balance'] = str(balanceint)
                with open('bankdata.json','w') as file:
                    json.dump(self.bankdata,file)  
            else:
                print("Your Balance is Not Enough!")
        else:
            print("Invalid Credentials!")
    def transferablebanks(self,user,currentbank):
        try:
            with open('bankdata.json','r') as file:
               self.bankdata= json.load(file)
        except:
            pass
        reslist = []
        for bank in self.bankdata[user]:
            if(not bank == currentbank):
                reslist.append(bank)
        return reslist
    def transfer(self,user,currentbank,targetbank,amount,pwd,cvv2):
        try:
            with open('bankdata.json','r') as file:
               self.bankdata= json.load(file)
        except:
            pass
        startbank = self.bankdata[user][currentbank]
        targetbank = self.bankdata[user][targetbank]
        targetbalance = int(targetbank['balance'])
        targetbalance += int(amount)
        startbankbalance = int(startbank['balance'])
        startbankbalance -= int(amount)
        startbank['balance'] = startbankbalance
        targetbank['balance'] = targetbalance
        with open('bankdata.json','w') as file:
            json.dump(self.bankdata,file)  
        return True

bnkinit = banksystem()