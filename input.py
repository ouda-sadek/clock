import time

def display_time(hours, minutes, seconds):
   
    while True:
       
        print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")

        
        time.sleep(1)

        
        seconds += 1

        
        if seconds == 60:
            seconds = 0
            minutes += 1

        
        if minutes == 60:
            minutes = 0
            hours += 1

        
        if hours == 24:
            hours = 0


def set_time():
    
    while True:
        try:
         
            user_input = input("Enter the initial time in the format hh:mm:ss: ")
            hours, minutes, seconds = map(int, user_input.split(":"))

            
            if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
                return hours, minutes, seconds
            else:
                print("Please enter a valid time (hh between 0-23, mm and ss between 0-59).")
        except ValueError:
            print("Invalid format. Please enter the time in the format hh:mm:ss.")

if __name__ == "__main__":
   
    hours, minutes, seconds = set_time()

    
    display_time(hours, minutes, seconds)
