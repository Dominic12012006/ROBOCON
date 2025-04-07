#QUADRATIC FIT
from ultralytics import YOLO
import numpy as np
import math
import cv2
# from scipy.optimize import curve_fit
model = YOLO('best.pt')
cap = cv2.VideoCapture(0)
actual_distances = np.array([325,353,400,286,251,191,159])  # meters
measured_distances = np.array([325,355,418,286,243,186,145])

coefficients = np.polyfit(measured_distances, actual_distances, 2)  # quadratic fit

def corrected_distance(measured_distance):
    return coefficients[0] * measured_distance**2 + coefficients[1] * measured_distance + coefficients[2]

while True:
    ret, frame = cap.read()
    if not ret:
        break
    

    results = model.predict(source = frame,conf=0.25,save=True)
    for i in results:
        for box in i.boxes:
            x_center, y_center, width, height = box.xywh[0].cpu().numpy()
            x_center, y_center, width, height = (
                float(x_center),
                float(y_center),
                float(width),
                float(height),
            )
        
            #confidence = float(box.conf[0].cpu().numpy())
            class_id = int(box.cls[0].cpu().numpy())
            class_name = results[0].names.get(class_id, "Unknown")
            
            if class_name == "basket":
                unit_length = 50/ width #returns in cm (47.2 cm is outer diameter of hoop)
                const = 1215
                measured_distance = unit_length * const
                distance=corrected_distance(measured_distance)
                distance = round(distance, 2)
                print(f"Distance to basket: {distance:.2f} centimeters")
                xmin=x_center-(width/2)
                ymin=y_center-(height/2)

                xmax=x_center+(width/2)
                ymax=y_center+(height/2)

                confidence=round(box.conf[0].item(),3)
                frame=cv2.rectangle(frame,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(255,0,0),2)
                xoffset=x_center-320
                if xoffset>-3 and xoffset<3:#angle is almost correct
                    s="safe" 
                else:
                    s="unsafe"
                cv2.putText(frame,s,(320,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                cv2.putText(frame,str(distance),(500,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                cv2.putText(frame,str(confidence),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                #to calculate constant
                #f=500/unit_length #for cm #from 5m away
                #print(f)
            
            cv2.imshow("distance",frame)
            if cv2.waitKey(1)==ord('q'):
                break
cap.release()
cap.destroyAllWindows()
