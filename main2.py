import cv2
import numpy as np

# Load the monochrome image
image_path = "circle_monochrome.jpg"  # Replace with the actual image path
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Perform Gaussian blur to reduce noise (optional but can improve results)
blurred_image = cv2.GaussianBlur(image, (9, 9), 2)

# Detect circles using Hough Circle Transform
circles = cv2.HoughCircles(
    blurred_image,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=20,
    param1=50,
    param2=30,
    minRadius=0,
    maxRadius=0,
)

# If circles were found
if circles is not None:
    circles = np.uint16(np.around(circles))
    biggest_circle = circles[0][0]  # Initialize with the first detected circle
    max_radius = 0

    for circle in circles[0]:
        x, y, radius = circle
        if radius > max_radius:
            max_radius = radius
            biggest_circle = circle

    x, y, radius = biggest_circle
    print("Biggest circle:")
    print("Center: ({}, {})".format(x, y))
    print("Radius:", radius)

    # Draw the detected circle
    circle_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.circle(circle_image, (x, y), radius, (0, 255, 0), 2)
    cv2.imshow("Biggest Circle", circle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No circles were found.")

