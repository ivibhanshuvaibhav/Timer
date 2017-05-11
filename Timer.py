import time as Time
from playsound import playsound
from pync import Notifier

path = 'early-sunrise.mp3'

time = input("Enter time (in seconds):")

print 'Your timer has been set for' , time , 'seconds'

for i in reversed(range(1,time)):
    print 'Time left is', i , 'seconds'
    Time.sleep(1)

text = str(time) + ' seconds has been completed'
print text
Notifier.notify(text, title='Timer')

playsound(path, block=False)
Time.sleep(10)
exit()