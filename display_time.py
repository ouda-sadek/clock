import time

# Get the current time
current_time = time.localtime()
hours = current_time.tm_hour
minutes = current_time.tm_min
seconds = current_time.tm_sec

try:
    while True:
        
        # Format the time as hh:mm:ss
        formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
        
        # Display the time, overwriting the previous line
        print(formatted_time, end="\r", flush=True)

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
