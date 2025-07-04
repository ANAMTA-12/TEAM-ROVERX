import cv2
import numpy as np

# Load the image
img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Color Theory
def color_theory():
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow("BGR", img)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("HSV", hsv)

# 2. Histogram Equalization
def histogram_equalization():
    equalized = cv2.equalizeHist(gray)
    cv2.imshow("Original Gray", gray)
    cv2.imshow("Equalized", equalized)

# 3. Thresholding
def thresholding():
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    adaptive = cv2.adaptiveThreshold(gray, 255, 
                                     cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)
    cv2.imshow("Binary Threshold", binary)
    cv2.imshow("Adaptive Threshold", adaptive)

# 4. Contrast and Brightness
def contrast_brightness():
    adjusted = cv2.convertScaleAbs(img, alpha=1.5, beta=40)
    cv2.imshow("Contrast & Brightness", adjusted)

# 5. Smoothing (Blurring)
def smoothing():
    avg = cv2.blur(img, (5, 5))
    gauss = cv2.GaussianBlur(img, (5, 5), 0)
    median = cv2.medianBlur(img, 5)
    cv2.imshow("Average Blur", avg)
    cv2.imshow("Gaussian Blur", gauss)
    cv2.imshow("Median Blur", median)

# 6. Dilation and Erosion
def morph_ops():
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(binary, kernel, iterations=1)
    erosion = cv2.erode(binary, kernel, iterations=1)
    cv2.imshow("Dilation", dilation)
    cv2.imshow("Erosion", erosion)

# 7. Sharpening
def sharpening():
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    sharpened = cv2.filter2D(img, -1, kernel)
    cv2.imshow("Sharpened", sharpened)

# 8. Geometric Transformations
def geometric_transform():
    rows, cols = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)  # Rotate 45 degrees
    rotated = cv2.warpAffine(img, M, (cols, rows))
    flipped = cv2.flip(img, 1)  # Horizontal flip
    cv2.imshow("Rotated", rotated)
    cv2.imshow("Flipped", flipped)

# 9. Edge Detection
def edge_detection():
    edges = cv2.Canny(gray, 100, 200)
    cv2.imshow("Canny Edges", edges)

# 10. Contours
def contours():
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img_contours = img.copy()
    cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 2)
    cv2.imshow("Contours", img_contours)

# 11. Corner Detection
def corner_detection():
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners = np.int0(corners)
    corner_img = img.copy()
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(corner_img, (x, y), 4, (0, 255, 0), -1)
    cv2.imshow("Corners", corner_img)

# 12. Image Fusion
def image_fusion():
    img2 = cv2.imread("test.jpg")
    img2 = cv2.GaussianBlur(img2, (21, 21), 0)
    fused = cv2.addWeighted(img, 0.7, img2, 0.3, 0)
    cv2.imshow("Image Fusion", fused)

# 13. Convolution
def convolution():
    kernel = np.ones((5, 5), np.float32) / 25
    conv = cv2.filter2D(img, -1, kernel)
    cv2.imshow("Convolution (Custom Filter)", conv)


# color_theory()
# histogram_equalization()
# thresholding()
# contrast_brightness()
# smoothing()
# morph_ops()
# sharpening()
# geometric_transform()
# edge_detection()
# contours()
# corner_detection()
# image_fusion()
# convolution()

# ------------------------------------------------------

cv2.waitKey(0)
cv2.destroyAllWindows()