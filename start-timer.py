import threading
import time
import simpleaudio as sa
import datetime

def timerdone(tick):
    outputtxt(str(datetime.timedelta(seconds=tick))[-5:])
    time.sleep(1)

def outputtxt(string):
    f = open("/home/justin/timer.txt","w")
    f.write(string)
    f.close()

def readTimer():
    f = open("/home/justin/timer.txt","r")
    settime = f.read()
    f.close()
    return settime

time_sec=int(readTimer())*60
timer = threading.Thread(target=timerdone)
for i in range(time_sec,0,-1):
    timer = threading.Thread(target=timerdone, args=(i,))
    timer.start()
    timer.join()

outputtxt(" Done!")

filename = '/home/justin/Music/alarm-cleaner.wav'
wave_obj = sa.WaveObject.from_wave_file(filename)
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing

outputtxt(str(time_sec))
