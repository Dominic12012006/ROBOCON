import cv2 as cv
from cv2 import aruco
import numpy as np

MARKER_SIZE = 19.7  # cm

marker_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
param_markers = aruco.DetectorParameters()

# Assumed focal length (you may need to calibrate this for accurate results)
FOCAL_LENGTH = 593  # Adjust based on camera

cap = cv.VideoCapture(0)
# cap = cv.VideoCapture('http://192.0.0.4:8080/video') # Uncomment for IP camera

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, _ = aruco.detectMarkers(gray_frame, marker_dict, parameters=param_markers)
    
    if marker_corners:
        for ids, corners in zip(marker_IDs, marker_corners):
            cv.polylines(frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA)
            
            corners = corners.reshape(4, 2).astype(int)
            top_right = corners[0].ravel()
            bottom_right = corners[2].ravel()
            
            # Compute distance using marker size and focal length
            pixel_width = np.linalg.norm(corners[0] - corners[1])  # Distance between top-right and top-left
            distance = (MARKER_SIZE * FOCAL_LENGTH) / pixel_width if pixel_width > 0 else 0
            # c=30*pixel_width/MARKER_SIZE if pixel_width > 0 else 0
            cv.putText(
                frame,
                f"ID: {ids[0]} Dist: {round(distance, 2)}cm",
                top_right,
                cv.FONT_HERSHEY_PLAIN,
                3,
                (0, 255, 255),
                2,
                cv.LINE_AA,
            )
    
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
