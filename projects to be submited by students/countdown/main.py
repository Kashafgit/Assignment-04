import time
import winsound
seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    min,sec = divmod(seconds, 60)
    timer = f"{min:02d}:{sec:02d}"
    print(timer, end="\r")
    time.sleep(1)
    seconds -=1
    
    
    
print("Times up")
winsound.Beep(1000,1000)

