import time

# Function to set and display the time
def display_time(hours, minutes, seconds, alarm_time):
    try:
        while True:
            # Format the time as hh:mm:ss
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            
            # Display the time, overwriting the previous line
            print(formatted_time, end="\r", flush=True)
            
            # Check if the current time matches the alarm time
            if (hours, minutes, seconds) == alarm_time:
                print("\nALARM! Time to wake up, Mamie Jeannine!")
                #break  

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

# Example of setting and displaying the time with an alarm
hours, minutes, seconds = 16, 30, 0  
alarm_time = (16, 30, 5)  

# Call the function to display and update the time, with the alarm
display_time(hours, minutes, seconds, alarm_time)
