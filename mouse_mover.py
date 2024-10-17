import random
import pyautogui
import time


def format_time(t):
    remainder = t
    hours = remainder // 3600
    remainder = remainder - (hours * 3600)
    minutes = remainder // 60
    remainder = remainder - (minutes * 60)
    seconds = int(remainder)

    return f"{hours}H {minutes}M {seconds}S"


def get_hours_input():
    input_query_string = "\n\nEnter a time in hours to move mouse for: "
    while 1:
        inp = input(input_query_string)
        try:
            inp = float(inp)
            if inp > 24:
                print("Cannot work for more than 24 hours!")
                continue
            if inp < 0.00001:
                print("Cannot work for negative hours!")
                continue

            return inp
        except:
            print("Hour input must be castable to a float!")


run_hours = get_hours_input()
run_duration = run_hours * 60 * 60
start_time = time.time()

while time.time() - start_time < run_duration:
    time_left = start_time + run_duration - time.time()
    print(f"time left: {format_time(time_left)}")
    screen_width, screen_height = pyautogui.size()
    x = random.randint(0, screen_width - 1)
    y = random.randint(0, screen_height - 1)
    pyautogui.moveTo(x, y, duration=0.6)
    time.sleep(random.randint(20, 30))

print("Finished moving the mouse.")
