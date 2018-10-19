from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

is_logging = True
log_dir = "logs\\"
current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
log_name = log_dir+current_time + " KEYS.log"

logging.basicConfig(filename=(log_name), level=logging.DEBUG, format='%(asctime)s: %(message)s')
print("Logging has started")
def on_press(key):
    global is_logging
    if is_logging:
        logging.info(str(key))
    print(key)
    if key == Key.end:
        print('found')
        return False
    if key == Key.esc:
        if is_logging:
            print("Paused logging")
        else:
            print('Started logging again')
        is_logging = not is_logging
        print(is_logging)

with Listener(on_press=on_press) as listener:
    listener.join()

