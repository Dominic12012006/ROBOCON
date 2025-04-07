from ultralytics import YOLO
import cv2
from distance import calcdist
from coords import coordinate
from equation import calcrpm
import time

# Load your YOLO model and initialize video capture
model = YOLO(r'C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\best.pt')
cap = cv2.VideoCapture(0)

# Initial coordinates (starting at origin)
oxcoord, oycoord = 0, 0
xcoord, ycoord = 0, 0

HFOV = 65.0          # Horizontal field-of-view in degrees
FRAME_WIDTH = 640    # Image width in pixels

def pixel_offset_to_angle(x_offset):
    """
    Convert a pixel offset (from the image center) into an angle in degrees.
    Assumes a linear mapping based on the camera's HFOV.
    """
    return (x_offset * HFOV) / FRAME_WIDTH




while True:
    # Check for Pygame events to allow window closing
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=0.25, save=True)
    detected = False
    for i in results:
        for box in i.boxes:
            # Extract bounding box parameters
            x_center, y_center, width, height = box.xywh[0].cpu().numpy()
            x_center, y_center, width, height = float(x_center), float(y_center), float(width), float(height)
            
            class_id = int(box.cls[0].cpu().numpy())
            class_name = results[0].names.get(class_id, "Unknown")
            
            if class_name == "basket":
                detected = True
                # Calculate distance to basket and required RPM
                distance = calcdist(width)
                print(f"Distance to basket: {distance:.2f} centimeters")
                rpm = calcrpm(120, 243, distance, 58.03, 6.35)
                
                # Calculate bounding box coordinates
                xmin = x_center - (width / 2)
                ymin = y_center - (height / 2)
                xmax = x_center + (width / 2)
                ymax = y_center + (height / 2)
                
                # Draw the bounding box on the frame
                cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 0, 0), 2)
                
                # Calculate angular error from the image center
                xoffset = round(x_center - 320, 1)
                angle = pixel_offset_to_angle(xoffset)
                cv2.putText(frame, f"Angle: {angle:.2f} deg", (10, 200),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                
                # Compute new bot coordinates based on the distance and angle
                xcoord, ycoord = coordinate(distance, angle)
                cv2.putText(frame, str(xcoord), (280, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                cv2.putText(frame, str(ycoord), (340, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                cv2.putText(frame, str(distance), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                cv2.putText(frame, str(xoffset), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                
                # Update the path with the new coordinates
                print(f"New coordinate appended: ({xcoord}, {ycoord})")  # Debug statement
                oxcoord, oycoord = xcoord, ycoord


    # Show the processed frame from OpenCV (for debugging)
    cv2.imshow("distance", frame)
    if cv2.waitKey(1) == ord('q'):
        running = False

    # Slow down the loop a little for better visualization

cap.release()
cv2.destroyAllWindows()
