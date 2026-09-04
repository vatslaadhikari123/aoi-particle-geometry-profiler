import cv2
import numpy as np
import matplotlib.pyplot as plt

def extract_roi(image, bbox):
    """Crops the detected particle bounding box out of the full image."""
    h_img, w_img = image.shape[:2]
    # bbox expected as [x_center, y_center, width, height] normalized (0-1)
    xc, yc, w, h = bbox
    x = max(0, int((xc - w / 2.0) * w_img))
    y = max(0, int((yc - h / 2.0) * h_img))
    box_w = min(w_img - x, int(w * w_img))
    box_h = min(h_img - y, int(h * h_img))
    return image[y:y + box_h, x:x + box_w]

def profile_particle(roi_bgr):
    """Performs adaptive thresholding, contour fitting, and radial ray audit."""
    gray = cv2.cvtColor(roi_bgr, cv2.COLOR_BGR2GRAY)
    
    # Adaptive threshold to isolate particle foreground
    binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 2
    )
    inv_binary = cv2.bitwise_not(binary)

    contours, _ = cv2.findContours(inv_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if not contours:
        return None

    largest_contour = max(contours, key=cv2.contourArea)
    (x, y), radius = cv2.minEnclosingCircle(largest_contour)
    center = (int(x), int(y))
    radius = int(radius)

    # Count pixels along the horizontal radius vector
    pixels_in_line = 0
    for i in range(radius):
        px = int(center[0] + i)
        py = int(center[1])
        if cv2.pointPolygonTest(largest_contour, (px, py), False) >= 0:
            pixels_in_line += 1

    return {
        "center": center,
        "radius": radius,
        "pixels_in_line": pixels_in_line,
        "binary_mask": inv_binary,
        "contour": largest_contour
    }
