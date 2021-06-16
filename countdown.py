# import the time module
import time
from datetime import datetime
  
# main() function to call countdown()
def main():
    dateInput = input('Enter future date {MMM DD YYYY HH:MM}: ')
    countdown(dateInput)

# define the countdown func.
def countdown(dateInput):
    
    timer = True
    
    while timer:
        
        # mins, secs = divmod(t, 60)
        # timer = '{:02d}:{:02d}'.format(mins, secs)
        # print(timer, end="\r")
        # time.sleep(1)
        # t -= 1
        
        banner = '''
        
 ██████╗ ██████╗  █████╗ ██████╗ ██╗   ██╗ █████╗ ████████╗██╗ ██████╗ ███╗   ██╗██╗
██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██║   ██║██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║██║
██║  ███╗██████╔╝███████║██║  ██║██║   ██║███████║   ██║   ██║██║   ██║██╔██╗ ██║██║
██║   ██║██╔══██╗██╔══██║██║  ██║██║   ██║██╔══██║   ██║   ██║██║   ██║██║╚██╗██║╚═╝
╚██████╔╝██║  ██║██║  ██║██████╔╝╚██████╔╝██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║██╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝
                                                                                 
        '''
        
        graduation = 'Dec 17 2021 00:00'
        if dateInput == 'graduation':
            dateInput = graduation
        futuredate = datetime.strptime(dateInput, '%b %d %Y %H:%M')
        nowdate = datetime.now()
        diff = futuredate - nowdate
        count_hours, rem = divmod(diff.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        count = int((futuredate-nowdate).total_seconds())
        
        days = count//86400
        hours = (count-days*86400)//3600
        minutes = (count-days*86400-hours*3600)//60
        seconds = count-days*86400-hours*3600-minutes*60
        
        # count_hours -= 1
        # count_minutes -= 1
        # count_seconds -= 1
        
        #timer2 = " --> {:02d} days {:02d}:{:02d}:{:02d} left".format(diff.days, count_hours, count_minutes, count_seconds)
        
        #print(timer2, end="\r")
        print(f" --> {diff.days} days {hours}:{minutes}:{seconds} left ", end='\r')
        time.sleep(1)
        
        if diff.days == 0 and hours == 0 and minutes == 0 and seconds == 0:
            print(f'\n {banner}')
            exit(0)
    
    timer = False
    
  
# input time in seconds
# t = input("Enter the time in seconds: ")
  
# Call main()
if __name__ == '__main__':
    main()