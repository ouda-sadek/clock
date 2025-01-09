import time

alarm_time = input("Enter the time of alarm to be set:HH:MM:SS: ")
alarm_hour, alarm_minute, alarm_second = alarm_time.split(':')
alarm_hour = int(alarm_hour)
alarm_minute = int(alarm_minute)
alarm_second = int(alarm_second)

print("Setting up alarm...")

while True:
    current_time = time.localtime()
    current_hour = current_time.tm_hour
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec
    if alarm_hour == current_hour and alarm_minute == current_minute and alarm_second == current_second:
        print("Wake Up!")
        break
    print(f" {current_hour}:{current_minute}:{current_second}")
    time.sleep(1)