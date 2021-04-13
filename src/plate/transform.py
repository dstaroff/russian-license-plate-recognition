import cv2
import numpy as np


def get_grayed_and_thresholded(image):
    img = cv2.resize(image.copy(), (520, 112))

    gray = cv2.bilateralFilter(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 13, 15, 15)
    blurred = cv2.medianBlur(gray, 5)
    _, thresholded = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresholded


def get_rotated(image):
    thresholded = get_grayed_and_thresholded(image)

    contours, _ = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the rotated rectangles
    maxRect = None
    for c in contours:
        if maxRect is not None:
            if cv2.contourArea(c) > cv2.contourArea(maxRect):
                maxRect = c
        else:
            maxRect = c

    maxRect = cv2.minAreaRect(maxRect)

    angle = maxRect[2]

    if angle > 45:
        angle -= 90

    M = cv2.getRotationMatrix2D(maxRect[0], angle, 1.0)
    h, w = thresholded.shape[:2]
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    return cv2.warpAffine(thresholded, M, (nW, nH))


def get_clean(image):
    rotated = get_rotated(image)

    contours, _ = cv2.findContours(rotated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the rotated rectangles
    maxRect = None
    for c in contours:
        if maxRect is not None:
            if cv2.contourArea(c) > cv2.contourArea(maxRect):
                maxRect = c
        else:
            maxRect = c

    maxRect = cv2.minAreaRect(maxRect)
    box = np.intp(cv2.boxPoints(maxRect))

    min_x = min(box[i][0] for i in range(len(box)))
    min_y = min(box[i][1] for i in range(len(box)))
    max_x = max(box[i][0] for i in range(len(box)))
    max_y = max(box[i][1] for i in range(len(box)))

    plate_img = rotated[min_y:max_y, min_x:max_x].copy()

    return cv2.resize(plate_img, (520, 112))
