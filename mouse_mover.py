import pyautogui
import random
import time

def format_time(t):
    remainder = t
    hours = remainder // 3600
    remainder = remainder - (hours * 3600)
    minutes = remainder // 60
    remainder = remainder - (minutes * 60)
    seconds = int(remainder)

    return f'{hours}H {minutes}M {seconds}S'



# Set the duration to run the script (in seconds)
run_hours = 2
run_duration = run_hours * 60 * 60  
start_time = time.time()

while time.time() - start_time < run_duration:
    time_left = start_time + run_duration - time.time()
    print(f'time left: {format_time(time_left)}')
    
    # Get screen width and height
    screen_width, screen_height = pyautogui.size()

    # Generate random x and y coordinates within the screen dimensions
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)

    # Move the mouse to the random coordinates
    pyautogui.moveTo(x, y, duration=3)  # Smooth movement over 0.5 seconds

    # Wait for 10 seconds before the next move
    time.sleep(6)

print("Finished moving the mouse.")
