import time

#Function to check if the current time matches the alarm time
def check_alarm_time(alarm_time, hours, minutes, seconds):
    if (hours == alarm_time[0] and minutes == alarm_time[1] and seconds == alarm_time[2]):
        return True
    return False

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

# Get the current time
current_time = time.localtime()
hours = current_time.tm_hour
minutes = current_time.tm_min
seconds = current_time.tm_sec

# Function to update and display the time
def display_time(hours, minutes, seconds, alarm_time):
    try:
        while True:
            # Format the time as hh:mm:ss
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
        
            # Display the time, overwriting the previous line
            print(formatted_time, end="\r", flush=True)

            # Check if the current time matches the alarm time
            if check_alarm_time(alarm_time, hours, minutes, seconds):
                # show the alarm time 5 seconds
                for _ in range(5):
                    print("ALARM! Time to wake up, Mamie Jeannine!")
                    time.sleep(1)  
                
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

    # Call function to display and update time
    display_time(hours, minutes, seconds, alarm_time)

# Start the program
if __name__ == "__main__":
    main()