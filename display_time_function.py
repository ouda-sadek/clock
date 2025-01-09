import time

#initialize time
print ("00:00:00")

# Get the time from user input in the format hh:mm:ss
user_time = input("Enter hours, minutes and seconds in the format hh:mm:ss: ").split(":")
hours = int(user_time[0])
minutes = int(user_time[1])
seconds = int(user_time[2])

# Get the alarm_time from user input in the format hh:mm:ss
alarm_time = input("Enter alarm_time_hours, alarm_time_minutes and alarm_time_seconds in the format hh:mm:ss: ").split(":")
alarm_time_hours = int(alarm_time[0])
alarm_time_minutes = int(alarm_time[1])
alarm_time_seconds = int(alarm_time[2])

#function to check alarm_time 
def check_alarm_time(alarm_time, hours, minutes, seconds):
   if (hours == alarm_time_hours and minutes == alarm_time_minutes and seconds == alarm_time_seconds):
        return True
   return False

# Function to set and display the time
def display_time(hours, minutes, seconds, alarm_time):
        try:
            while True:
                # Format the time as hh:mm:ss
                formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            
                # Display the time, overwriting the previous line
                print(formatted_time, end="\r", flush=True)

                # Check if the current time matches the alarm time
                if check_alarm_time(alarm_time, hours, minutes, seconds):
                    for _ in range(5):
                        print("ALARM! Time to wake up, Mamie Jeannine!")
                    #break
                        seconds += 1
            
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



# Call the function to display and update the time
display_time(hours, minutes, seconds, alarm_time)