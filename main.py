import pyautogui
from PIL import ImageGrab
import time
import threading

def scheduled_action():
    pyautogui.keyDown('space')
    time.sleep(0.3)
    pyautogui.keyUp('space')


def main():
    i = 0
    currents = [None] * 217
    white = (255, 255, 255, 255)
    cactusx = 600

    while True:
        i = i + 1
        print(i)
        start = time.time()
        screenshot1 = ImageGrab.grab(bbox=(180, 710, 1270, 711))
        screenshot2 = ImageGrab.grab(bbox=(180, 654, 1270, 655))
        end = time.time()
        delay = end - start
        currents1 = [screenshot1.getpixel((i * 5, 0)) for i in range(217)]
        currents2 = [screenshot2.getpixel((i * 5, 0)) for i in range(217)]

        for j in range(len(currents)):
            if currents1[j] != white or currents2[j] != white:
                cactusx = j * 5
                print(cactusx)
                waitime = max(0, (cactusx / 1000) - delay)

                if i > 80:
                    waitime = max(0, waitime * 0.75)
                if i > 150:
                    waitime = max(0, waitime * 0.7)
                if i > 280:
                    waitime = max(0, waitime * 0.7)
                if i > 450:
                    waitime = max(0, waitime * 0.8)
                if i > 800:
                    waitime = max(0, waitime * 0.75)
                if i > 1200:
                    waitime = max(0, waitime * 0.75)
                if i > 2000:
                    waitime = max(0, waitime * 0.9)

                timer = threading.Timer(waitime, scheduled_action)
                timer.start()
                break

if __name__ == "__main__":
    main()