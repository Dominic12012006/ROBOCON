from ultralytics import YOLO
import numpy as np
import cv2

# Load camera calibration data
calib_data = np.load('MultiMatrixp.npz')
camera_matrix = calib_data['camMatrix']
dist_coeffs = calib_data['distCoef']

# Extract focal length from camera matrix
focal_length = camera_matrix[0, 0]  # fx (in pixels)

# Known real-world dimensions of the basketball hoop
real_width = 50  # cm
real_height = 45  # Adjust based on hoop height

# Load YOLO model
model = YOLO(r'C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\best.pt')

# Read input image
image_path = r"C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\photos\IMG-20250317-WA0047.jpg"
frame = cv2.imread(image_path)

# Undistort image
undistorted_frame = cv2.undistort(frame, camera_matrix, dist_coeffs)

# Process frame with YOLO
results = model.predict(source=undistorted_frame, conf=0.25, save=True)

for res in results:
    for box in res.boxes:
        x_center, y_center, width, height = box.xywh[0].cpu().numpy()
        x_center, y_center, width, height = float(x_center), float(y_center), float(width), float(height)

        class_id = int(box.cls[0].cpu().numpy())
        class_name = results[0].names.get(class_id, "Unknown")

        if class_name == "basket":
            # Get bounding box coordinates
            xmin = x_center - (width / 2)
            ymin = y_center - (height / 2)
            xmax = x_center + (width / 2)
            ymax = y_center + (height / 2)

            # Use diagonal size instead of just width
            detected_diagonal = np.sqrt(width**2 + height**2)

            # Approximate distance using diagonal size
            real_diagonal = np.sqrt(real_width**2 + real_height**2)
            distance = (focal_length * real_diagonal) / detected_diagonal
            distance = round(distance, 2)

            confidence = round(box.conf[0].item(), 3)

            # Draw bounding box
            cv2.rectangle(
                undistorted_frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 0, 0), 2
            )

            # Display distance and confidence
            cv2.putText(undistorted_frame, f"Dist: {distance} cm", (500, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            cv2.putText(undistorted_frame, f"Conf: {confidence}", (20, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

cv2.imshow("Distance Estimation", undistorted_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
