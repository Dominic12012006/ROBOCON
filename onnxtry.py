import cv2
import numpy as np

# Load the ONNX model
net = cv2.dnn.readNetFromONNX(r"C:\Users\Happy Home\Downloads\hoop_best (1).onnx")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Assuming input size is 640x640 for YOLOv5/YOLOv8-style ONNX
INPUT_WIDTH = 640
INPUT_HEIGHT = 640
CONFIDENCE_THRESHOLD = 0

# List of class names (make sure it matches your model)
class_names = ["Basketball-Hoop"]  # Add more if needed

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Resize and normalize the frame for ONNX input
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (INPUT_WIDTH, INPUT_HEIGHT), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward()

    rows = outputs.shape[1]
    image_height, image_width = frame.shape[:2]

    for i in range(rows):
        row = outputs[0][i]
        confidence = row[4]
        if confidence >= CONFIDENCE_THRESHOLD:
            scores = row[5:]
            class_id = np.argmax(scores)
            if class_id >= len(class_names):
                continue
            class_name = class_names[class_id]
            if class_name != "Basketball-Hoop":
                continue

            # Extract bounding box
            cx, cy, w, h = row[0:4]
            x_center = int(cx * image_width / INPUT_WIDTH)
            y_center = int(cy * image_height / INPUT_HEIGHT)
            width = int(w * image_width / INPUT_WIDTH)
            height = int(h * image_height / INPUT_HEIGHT)

            xmin = int(x_center - width / 2)
            ymin = int(y_center - height / 2)
            xmax = int(x_center + width / 2)
            ymax = int(y_center + height / 2)

            # Estimate distance
            unit_length = 50 / width  # cm/pixel
            distance = 350 / unit_length

            xoffset = x_center - (image_width // 2)
            s = "safe" if -3 < xoffset < 3 else "unsafe"

            # Draw bounding box and text
            cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (255, 0, 0), 2)
            cv2.putText(frame, s, (320, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            cv2.putText(frame, f"{distance:.2f} cm", (500, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
            cv2.putText(frame, f"{confidence:.2f}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("distance", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
