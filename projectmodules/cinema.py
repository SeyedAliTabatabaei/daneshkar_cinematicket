import json
from datetime import datetime
import karbar as k
userobj = k.User()
now = datetime.now()
class managecinema:
    def __init__(self):
        try:
            with open("showtimes.json",'r') as showtimesdict:
                data = json.load(showtimesdict)
                self.data = data
        except:
            pass
    def showtimelist(self):
        mylist = self.data.keys()
        counter = 1
        res = {}
        amount = 100
        for movie in mylist:
            print(f' {counter}. Price : {amount}$ | Movie : {movie} | Time : {self.data[movie]['time']} | Seats Left : {self.data[movie]['seats_left']} | Age Limit : {self.data[movie]['age_limit']}')   
            res[counter] = movie
            counter += 1
        print(f'\n For Exit Type "exit" \n')    
        return res
    def book_seat(self,movie,user):
        amount = 100
        birthdaylist = userobj.getbirthdata(user)
        if(birthdaylist[1] == now.strftime('%m') and birthdaylist[2] == now.strftime("%d")):
            k.clear_terminal()
            amount = amount * 0.5
            print(f"Congrats! It's Your Birthday!!! ") 
            print(f"50% Discount Applied For Your Birthday ")
            print(f"Ticket Amount Will Be {amount} Instead Of {amount*2}")
        age_limit = self.data[movie]['age_limit']
        seats_left = self.data[movie]['seats_left']
        self.data[movie]['seats_left'] = int(seats_left) - 1
        time = self.data[movie]['time']
        age = int(now.strftime('%Y')) - int(birthdaylist[0])
        if(age >= age_limit):
                if(seats_left >= 1):
                    if(int(time) > int(now.strftime('%H'))):
                        k.clear_terminal()
                        print(f'Ticket Price : {amount}$ Successfully Payed!  - {movie} Movie At {time}:00 Reservation Completed! \n')
                        with open("showtimes.json",'w') as f:
                            json.dump(self.data,f)
                    else:
                        print(f"Sorry! You're {int(now.strftime('%H')) - int(time)} Hours Late!")
                else:
                    print("Sorry! There is Not Seats Left")
        else:
            k.clear_terminal()

            print(f"Sorry! You Have To Be Above {age_limit} Years Old To Watch This Movie! \n")
    def apply_discount(self,user):
        pass