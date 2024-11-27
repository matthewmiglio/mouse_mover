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


def calc_new_pos(screen_width, screen_height):
    current_pos = pyautogui.position()
    current_x, current_y = current_pos
    new_x = current_x + random.randint(-2, 2)
    new_y = current_y + random.randint(-2, 2)

    if new_x < 0 or new_x > screen_width or new_y < 0 or new_y > screen_height:
        return calc_new_pos(screen_width, screen_height)

    return new_x, new_y


def main():

    run_hours = get_hours_input()
    run_duration = run_hours * 60 * 60
    start_time = time.time()
    screen_width, screen_height = pyautogui.size()

    while time.time() - start_time < run_duration:
        time_left = start_time + run_duration - time.time()
        print(f"time left: {format_time(time_left)}")
        pyautogui.moveTo(*calc_new_pos(screen_width, screen_height), duration=0.2)
        time.sleep(random.randint(50, 60))

    print("Finished moving the mouse.")


if __name__ == "__main__":
    main()
