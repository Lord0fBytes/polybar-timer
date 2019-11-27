# polybar-timer
Creates a Timer for Polybar and allows limited control

## Disclaimer:
 - This is like pre-pre-waybefore-alpha version
 - I am very very new to polybar and intermediate with python (I would love tips)
 - Will be cleaning it up as I can. 
 - It 'works', but only tested on my specific system (see below)
 
 ## Requirements:
  - [Python3](https://www.python.org/downloads/) (I am using 3.6.9)
    - [Simpleaudio](https://pypi.org/project/simpleaudio/) 
  - [Polybar](https://github.com/polybar/polybar)
  - Debian/Bash shell (I am using KDE Neon)

## Installation:
 - Create a folder called `timer` where ever you want this to run (mine is in `/home/$USER/timer`)
   - This will be where all the scripts reside for the polybar so note it mentally
 - Create a file called `timer.txt` in the folder above (in Debian `touch timer.txt`) 
   - This is where the timer's time is stored (more on this later)
 - Clone the `start_timer.py` file into the directory above
   - This is what runs the timer and writes to the `timer.txt` file
   - Polybar will be running an interval script that reads this file
 - Open your `config` file for polybar
   - 'Generally' it can be located here `/home/$USER/.config/polybar/config`
 - Add the following module in the polybar `config` file:
 ```
[module/timer]
type=custom/script
exec=echo Timer: `cat ~/timer/timer.txt`
interval=1
label=%output%
click-left=python3 ~/timer/timer.py &
click-middle=echo 0 > ~/timer.txt
click-right=kill $(pgrep python3) && echo 5 > ~/timer/timer.txt
scroll-up=echo $((1+`cat ~/timer.txt`)) > ~/timer/imer.txt
scroll-down=echo $((`cat ~/timer.txt`-1)) > ~/timer/timer.txt
 ```
 - Change the `~/timer/` to the absolute path from the folder you created in the first step
 - Dont forget to add the module to the bar
 - Save the config and reload the polybar (if needed)
 - You should now be able to use the timer function (hopefully)
 
## Usage Guide:
The polybar `config` file will run the python script every second which will grab the current time remaining and subtract 1 from it and the sleep for 1 second. 

- **Left Click** - This will start the timer using the python script
- **Right Click** - This will stop the timer at the current time (Note at the time of this writing it will also kill any Python3 apps or scripts you might be running in the background. Use at your own risk!)
- **Middle Click** - Resets the timer to 0 in the `timer.txt` file (when in doubt or it's not working start here)
- **Scroll Up** - Increases the timer by 1 minute
- **Scroll Down** - Decrease the timer by 1 minute

## TODO:
 - Clean up the code (a lot)
 - Make a nice argumented script that handles the controls instead of hard coded bash commands
 - Make everything in python maybe
 - Fix holes that stop this from working
 
## Final Words:
I appreciate you looking and this and I know it is not much, but I hope to make this useful enough to add to the polybar User Defined modules. I am super new to all this stuff so any critisim would be very welcome as long as you can point me in the direction of how to make it better. 

Open any issue you would like and I will try to fix it. 
