from time import sleep
import cv2


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
            print(fadein)
        img1 = img2
        sleep(5)


if __name__ == "__main__":
    img1 = cv2.imread("/Users/alkis/Desktop/Screenshot 2023-07-03 at 9.24.14 AM.png")
    img2 = cv2.imread("/Users/alkis/Desktop/Screenshot 2023-07-03 at 9.24.11 AM.png")
    fade_in([img1, img2, img1])
