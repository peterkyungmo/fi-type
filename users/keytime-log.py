import time
from pynput import keyboard

# Log file name
log_file = "key_log.txt"

# List to store keypress data
key_log = []

# Variable to track the time of the last key press
last_time = None

def on_press(key):
    global last_time
    try:
        # Record the current time
        current_time = time.time()

        # Determine the time difference between key presses
        if last_time is None:
            time_diff = 0
        else:
            time_diff = current_time - last_time

        # Update the last_time variable
        last_time = current_time

        # Record the key press and time difference
        key_data = (key.char if hasattr(key, 'char') and key.char else str(key), time_diff * 1000)
        key_log.append(key_data)

        # Check if "quit" has been typed
        if len(key_log) >= 4 and ''.join(k[0] for k in key_log[-4:]) == "quit":
            return False

    except Exception as e:
        print(f"Error: {e}")

def write_to_file():
    with open(log_file, "w") as file:
        for key, time_diff in key_log:
            file.write(f"Key: {key}, Time since last key: {time_diff:.4f} ms\n")

def main():
    print("Start typing. Type 'quit' to stop and save the log.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    print("Saving key log to file...")
    write_to_file()
    print(f"Log saved to {log_file}")

if __name__ == "__main__":
    main()
