import cv2
import numpy as np

def quality_checker(img):
    gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()
    is_clear = blur_score > 100
    return is_clear, round(blur_score,2)
def brightness_check(img):
    gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    mean_brightness = gray.mean()
    if mean_brightness < 80:
        return 'too dark'
    elif mean_brightness < 180:
        return 'good'
    else:
        return 'overly exposed'
     


