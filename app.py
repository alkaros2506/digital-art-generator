import cv2
from utils import generator, fade

if __name__ == "__main__":
    # generate images
    images = generator.get_n_images(8)
    # fade between images
    fade.fade_in([cv2.imread(image["filename"]) for image in images])
