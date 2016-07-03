import webbrowser
import time

n=1
startTime = time.ctime()
print("This program started on " + startTime)
while n<=3:
    time.sleep(2)
    webbrowser.open("https://www.youtube.com/watch?v=M6a2fMRwhhA")
    n = n+1

lasted = startTime - time.ctime()
print("This program laster " + lasted)
