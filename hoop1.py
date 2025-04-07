from ultralytics import YOLO
import numpy as np
import cv2

# Load camera calibration data
calib_data = np.load('MultiMatrixp.npz')
camera_matrix = calib_data['camMatrix']
dist_coeffs = calib_data['distCoef']

# Extract focal length from camera matrix
focal_length = camera_matrix[0, 0]  # fx (in pixels)

# Known real-world width of the basketball hoop (in cm)
real_width = 50 #47.2  

# Load YOLO model
model = YOLO(r'C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\best.pt')

# Open camera
cap = cv2.VideoCapture(r"C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\photos\IMG-20250317-WA0049.jpg")
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Undistort the frame using camera calibration parameters
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
                # Calculate distance using focal length and real-world width
                distance = (focal_length * real_width) / width
                distance = round(distance, 2)

                print(f"Distance to basket: {distance:.2f} cm")

                xmin = x_center - (width / 2)
                ymin = y_center - (height / 2)
                xmax = x_center + (width / 2)
                ymax = y_center + (height / 2)

                confidence = round(box.conf[0].item(), 3)
                undistorted_frame = cv2.rectangle(
                    undistorted_frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 0, 0), 2
                )

                xoffset = x_center - 320  # Assuming a 640-pixel width
                s = "safe" if -3 < xoffset < 3 else "unsafe"
                cv2.putText(undistorted_frame, s, (320, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                cv2.putText(undistorted_frame, f"Dist: {distance} cm", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                cv2.putText(undistorted_frame, f"Conf: {confidence}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    
    cv2.imshow("Distance Estimation", undistorted_frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
