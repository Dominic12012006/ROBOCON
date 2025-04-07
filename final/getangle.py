import cv2
import numpy as np
import math
from ultralytics import YOLO

# Load your trained YOLO model (adjust the path as needed)
model = YOLO(r'C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\best.pt')

# Known camera parameters
HFOV = 65.0          # horizontal field-of-view in degrees
FRAME_WIDTH = 640    # image width in pixels

def pixel_offset_to_angle(x_offset):
    """
    Convert a pixel offset (from the image center) into an angle in degrees.
    Assumes a linear mapping based on the camera's HFOV.
    """
    return (x_offset * HFOV) / FRAME_WIDTH

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise Exception("Could not open video device")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame to known width for consistency
        frame = cv2.resize(frame, (FRAME_WIDTH, int(frame.shape[0] * FRAME_WIDTH / frame.shape[1])))
        
        # Use YOLO model to detect objects
        results = model.predict(source=frame, conf=0.25, verbose=False)
        
        # For each detection in the first result (assuming single frame prediction)
        xoffset = None  # reset xoffset for each frame
        for r in results:
            for box in r.boxes:
                # Get bounding box center and dimensions
                x_center, y_center, width, height = box.xywh[0].cpu().numpy()
                x_center = float(x_center)
                y_center = float(y_center)
                width = float(width)
                height = float(height)
                
                class_id = int(box.cls[0].cpu().numpy())
                class_name = r.names.get(class_id, "Unknown")
                
                if class_name == "basket":
                    # Draw bounding box for visualization
                    xmin = int(x_center - (width / 2))
                    ymin = int(y_center - (height / 2))
                    xmax = int(x_center + (width / 2))
                    ymax = int(y_center + (height / 2))
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
                    
                    # Calculate the x offset from the image center (assume center is at FRAME_WIDTH/2)
                    xoffset = x_center - (FRAME_WIDTH / 2)
                    
                    # Optionally display the x offset on the frame
                    cv2.putText(frame, f"x offset: {xoffset:.1f}", (xmin, ymin - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                    break  # stop after finding the first basket
        
        if xoffset is not None:
            # Convert pixel offset to an angular error
            angle = pixel_offset_to_angle(xoffset)
            # Display the calculated values on the frame
            cv2.putText(frame, f"Angle: {angle:.2f} deg", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        else:
            # If basket not detected, indicate so.
            cv2.putText(frame, "Basket not detected", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        cv2.imshow("Video Feed", frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
 