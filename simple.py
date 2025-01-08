import time
while True:
    localtime = time.localtime()
    result = time.strftime("%H : %M : %S %p", localtime)
    print(result, end="\r", flush=True)
    time.sleep(1)