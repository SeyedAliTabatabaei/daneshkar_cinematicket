import argparse
import json

parser = argparse.ArgumentParser(description='Create a new showtime')
parser.add_argument('username', type=str, help='admin username')
parser.add_argument('movie', type=str, help='movie name')
parser.add_argument('time', type=str, help='time of the show')
parser.add_argument('seats_left', type=int, help='available seats count')
parser.add_argument('age_limit', type=int, help='age limit')
args = parser.parse_args()

adminuser = args.username
with open('showtimes.json','r') as f:
    shdata = json.load(f)

try:
    with open('data.json', "r") as showtimesfile:
        data = json.load(showtimesfile)
    if(adminuser in data):
        if(data[adminuser]['role'] == 'admin'):
            moviename = args.movie
            showtimedict = {
                'admin_name':args.username,
                'time':args.time,
                'seats_left':args.seats_left,
                'age_limit':args.age_limit,
            } 
            newdict = shdata
            newdict[moviename] = showtimedict
            try:
                with open('showtimes.json', "w") as showtimesfile:
                    json.dump(newdict , showtimesfile)
                print(f'Showtime added!')
            except:
                pass
       
        else:
            print("Sorry! You're Just a Normal User Not an Admin!")
        
except:
    pass




