import webbrowser
import time

i=0

print("The current time is "+time.ctime())
while(i<3):
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=8R3yb6ySl-o")
    i=i+1

