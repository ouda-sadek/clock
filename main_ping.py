import time

#Function to check if the current time matches the alarm time
def check_alarm_time(alarm_time, hours, minutes, seconds):
    if (hours == alarm_time[0] and minutes == alarm_time[1] and seconds == alarm_time[2]):
        return True
    return False
#Function to convert hour to 12 hour format with AM/PM 
def convert_to_12_hour_format(hours, minutes, seconds):
    period = "AM" if hours < 12 else "PM"
    hours = hours % 12
    if hours == 0:
        hours = 12
    return f"{hours:02}:{minutes:02}:{seconds:02} {period}"

# function to get the time from user input in the format hh:mm:ss
def set_time():
   
    while True:
        try:
            user_time = input("Enter hours, minutes and seconds in the format hh:mm:ss: ").split(":")
            hours = int(user_time[0])
            minutes = int(user_time[1])
            seconds = int(user_time[2])
            
            if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
                return hours, minutes, seconds
            else:
                print("Please enter a valid time (hh between 0-23, mm and ss between 0-59).")
        except ValueError:
            print("Invalid format. Please enter the time in the format hh:mm:ss.")

 

# function to get the alarm_time from user input in the format hh:mm:ss
def set_alarm():
    while True:
        try:
            alarm_time = input("Enter alarm time in the format hh:mm:ss: ").split(":")
            alarm_time_hours = int(alarm_time[0])
            alarm_time_minutes = int(alarm_time[1])
            alarm_time_seconds = int(alarm_time[2])
            
            if 0 <= alarm_time_hours < 24 and 0 <= alarm_time_minutes < 60 and 0 <= alarm_time_seconds < 60:
                return alarm_time_hours, alarm_time_minutes, alarm_time_seconds
            else:
                print("Please enter a valid alarm time (hh between 0-23, mm and ss between 0-59).")
        except ValueError:
            print("Invalid format. Please enter the alarm time in the format hh:mm:ss.")



# Function to update and display the time
def display_time(hours, minutes, seconds, alarm_time, mode_24h=True):
   try:
        while True:
           
            if mode_24h:
                formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            else:
                formatted_time = convert_to_12_hour_format(hours, minutes, seconds)
            
            # Display the time, overwriting the previous line
            print(formatted_time, end="\r", flush=True)

            # Check if the current time matches the alarm time
            if check_alarm_time(alarm_time, hours, minutes, seconds):
                for _ in range(5):
                    print(f"ALARM! Time to wake up Mamie Jeannine!",end="\r", flush=True)
                    time.sleep(0.5)
                    print("                                       ",end="\r", flush=True)
                    time.sleep(0.5)
                # After the alarm, add 5 seconds to the time
                seconds += 5

            # Increment the seconds
            seconds += 1

            # If seconds reach 60, reset to 0 and increment minutes
            if seconds == 60:
                seconds = 0
                minutes += 1

            # If minutes reach 60, reset to 0 and increment hours
            if minutes == 60:
                minutes = 0
                hours += 1

            # If hours reach 24, reset to 0 (24-hour clock)
            if hours == 24:
                hours = 0

            # Wait for 1 second before updating the time
            time.sleep(1)

   except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting...")

# Main function to manage the entire program
def main():
    print("00:00:00")
    hours, minutes, seconds = set_time()  
    alarm_time = set_alarm() 
    
    while True:
        mode = input("Choose time display mode (12 for 12-hour format, 24 for 24-hour format): ")
        if mode == "12":
            mode_24h = False
            break
        elif mode == "24":
            mode_24h = True
            break
        else:
            print("Invalid choice. Please enter '12' or '24'.") 

    # Call function to display and update time
    display_time(hours, minutes, seconds, alarm_time,mode_24h)

# Start the program
if __name__ == "__main__":
    main()