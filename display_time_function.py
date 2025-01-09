import time

#initialize time
print ("00:00:00")

# Get the time from user input in the format hh:mm:ss
valeurs = input("Enter hours, minutes and seconds in the format hh:mm:ss: ").split(":")
hours = int(valeurs[0])
minutes = int(valeurs[1])
seconds = int(valeurs[2])
# Function to set and display the time
def display_time(hours, minutes, seconds):
        try:
            while True:
                # Format the time as hh:mm:ss
                formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
            
                # Display the time, overwriting the previous line
                print(formatted_time, end="\r", flush=True)
            
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
display_time(hours, minutes, seconds)