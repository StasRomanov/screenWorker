import pyautogui
import time
import keyboard
import subprocess


# macbook sizes
# X = 0 - 1439
# Y = 0 - 899

# standard 1080p sizes:
# X:0 - 1919
# Y:0 - 1079

def screenshotWorker():
    i = 0

    while True:
        # example of actions
        # if pyautogui.position().x > 1400:
        #     print("ping arduino, send code 1->", i)
        # if pyautogui.position().x < 10:
        #     print("ping arduino, send code 0->", i)

        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(f"E:\\screenshots\\fileName{i}.png")  # path+name

        if i == 500:
            exit(0)
        time.sleep(5)
        i += 1


def screenCalibration():
    while True:
        print(f"mouse position: x:{pyautogui.position().x}, y:{pyautogui.position().y}")
        time.sleep(0.5)

# screenCalibration()
# screenshotWorker()
