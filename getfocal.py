from ultralytics import YOLO
import numpy
import math
import cv2

model = YOLO(r'C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\best.pt') 
cap = cv2.VideoCapture(1)
# cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Process frame with YOLO model prediction:
    results = model.predict(source=frame, conf=0.25, save=True)
    
    for res in results:
        for box in res.boxes:
            # Extract coordinates and other values
            x_center, y_center, width, height = box.xywh[0].cpu().numpy()
            x_center, y_center, width, height = float(x_center), float(y_center), float(width), float(height)
            
            class_id = int(box.cls[0].cpu().numpy())
            class_name = results[0].names.get(class_id, "Unknown")
            
            if class_name == "basket": 
                distance=350
                # Calculate distance using a constant diameter (47.2 cm) of the hoop
                unit_length = 50 / width  # cm per pixel (approx.)
                const = distance/unit_length  # your calibrated constant
                print(f"Distance to basket: {const:.2f} centimeters")
                
                # Calculate bounding box coordinates
                xmin = x_center - (width / 2)
                ymin = y_center - (height / 2)
                xmax = x_center + (width / 2)
                ymax = y_center + (height / 2)
                
                confidence = round(box.conf[0].item(), 3)
                frame = cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (255, 0, 0), 2)
                
                # Determine safety based on horizontal offset
                xoffset = x_center - 320  # assumes a 640-pixel width
                s = "safe" if -3 < xoffset < 3 else "unsafe"
                cv2.putText(frame, s, (320, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                cv2.putText(frame, str(const), (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                # cv2.putText(frame, str(confidence), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
                cv2.putText(frame, str(xoffset), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    
    cv2.imshow("distance", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
