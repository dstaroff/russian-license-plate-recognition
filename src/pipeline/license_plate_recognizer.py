import os

import cv2
import numpy as np

from src import plate
from src.local_utils.constants import (
    CHARACTERS_IMAGES_PATH,
    CHARACTERS_BEST_MODEL_FILE,
    CHARACTERS_SIZE,
)
from src.networks.character_classifier import CharacterClassifier
from src.plate import (
    LicensePlate,
    LicensePlateError,
)


class LicensePlateRecognizer:
    def __init__(self):
        self.classnames = os.listdir(CHARACTERS_IMAGES_PATH)
        self.model = CharacterClassifier(len(self.classnames))
        self.model.load_weights(CHARACTERS_BEST_MODEL_FILE)

    def recognize_license_plate(self, image, plate_rect):
        plate_image = plate.get_clean(image[
                                      plate_rect.y1:plate_rect.y2,
                                      plate_rect.x1:plate_rect.x2,
                                      ].copy()
                                      )

        plate_image = cv2.bitwise_not(plate_image)

        contours, _ = cv2.findContours(plate_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        crop_characters = []

        for contour in self.sort_contours(contours):
            x, y, w, h = cv2.boundingRect(contour)
            ratio = h / w

            if 1 <= ratio <= 3.5:
                if 0.5 <= h / plate_image.shape[0] <= 0.9:
                    curr_num = cv2.bitwise_not(plate_image[y:y + h, x:x + w].copy())
                    crop_characters.append(cv2.resize(curr_num, dsize=CHARACTERS_SIZE))

        if 8 <= len(crop_characters) <= 9:
            characters = [self.classnames[np.argmax(self.model.predict(self.image2data(img))[0])] for img in
                          crop_characters]
            try:
                return LicensePlate.from_characters(characters)
            except LicensePlateError:
                return None
        else:
            return None

    @staticmethod
    def sort_contours(contours, reverse=False):
        if len(contours) == 0:
            return contours

        i = 0
        boundingBoxes = [cv2.boundingRect(contour) for contour in contours]
        (contours, boundingBoxes) = zip(*sorted(zip(contours, boundingBoxes), key=lambda b: b[1][i], reverse=reverse))

        return contours

    @staticmethod
    def image2data(image):
        res = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

        return np.array([res.astype('float32') / 255])
