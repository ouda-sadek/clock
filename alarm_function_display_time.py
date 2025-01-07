import time

# Function to set the alarm
def set_alarm(time_tuple):
    return time_tuple

# Function to check if the current time matches the alarm time
def check_alarm(alarm, hours, minutes, seconds):
   if (hours == alarm[0] and minutes == alarm[1] and seconds == alarm[2]):
        return True
   return False

# Get the current time
current_time = time.localtime()
hours = current_time.tm_hour
minutes = current_time.tm_min
seconds = current_time.tm_sec

# Set the alarm 
alarm = set_alarm((21, 24, 00))

try:
    while True:
        # Format the time as hh:mm:ss
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
        print(formatted_time, end="\r", flush=True)

        # Check if the current time matches the alarm time
        if check_alarm(alarm, hours, minutes, seconds):
            print("\nALARM! Time to wake up, Mamie Jeannine!")
            #break

        # Increment the seconds counter
        seconds += 1
        # Handle rollover of minutes and hours
        if seconds == 60:
            seconds = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1
                if hours == 24:
                    hours = 0
        
        # Wait 1 second before updating the time
        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram interrupted. Exiting...")
