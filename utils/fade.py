import os
from time import sleep
import cv2


SLEEP_TIME = os.environ.get("SLEEP_TIME", 5)


def fade_in(images):  # pass images here to fade between
    img1 = images[0]
    x = 100
    for image in images[1:]:
        img2 = image
        for IN in range(0, x):
            fadein = IN / float(x)
            dst = cv2.addWeighted(img1, 1 - fadein, img2, fadein, 0)
            cv2.imshow("window", dst)
            cv2.waitKey(1)
        img1 = img2
        sleep(SLEEP_TIME)
