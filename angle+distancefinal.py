from ultralytics import YOLO
import numpy
import math
import cv2

model = YOLO('best.pt') 
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_width = frame.shape[1]

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
                unit_length = 47.2/ width #returns in cm (47.2 cm is outer diameter of hoop)
                const = 642
                angleconst=0.687
                distance = unit_length * const
                distance = round(distance, 2)
                print(f"Distance to basket: {distance:.2f} centimeters")
                xmin=x_center-(width/2)
                ymin=y_center-(height/2)

                xmax=x_center+(width/2)
                ymax=y_center+(height/2)

                confidence=round(box.conf[0].item(),3)
                frame=cv2.rectangle(frame,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(255,0,0),2)
                xoffset=x_center-(frame_width/2)
                if xoffset>-3 and xoffset<3:#angle is almost correct
                    s="safe" 
                else:
                    s="unsafe"
                
                angle=angleconst*xoffset
                angleconst=45/xoffset
                cv2.putText(frame,s,(320,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                cv2.putText(frame,str(distance),(500,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                cv2.putText(frame,str(confidence),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                cv2.putText(frame,str(angle),(20,150),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                print(angle)
                #to calculate constant
                #f=500/unit_length #for cm #from 5m away
                #print(f)
            
            cv2.imshow("distance",frame)
            if cv2.waitKey(1)==ord('q'):
                break
cap.release()
cap.destroyAllWindows()
