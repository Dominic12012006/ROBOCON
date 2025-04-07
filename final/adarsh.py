from ultralytics import YOLO
import cv2
from distance import calcdist
from coords import coordinate
import math
model = YOLO(r'C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\best.pt')
cap = cv2.VideoCapture(1)

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
                # angle=0
                distance=calcdist(width)
                
                g = 980.665  # Acceleration due to gravity (cm/s²)
                theta = math.radians(58.03)  # Fixed shooter angle (converted to radians)
                height = 123 # Height of the shooting mech to hoop (centimetres)
                r_wheel = 6.35  # Radius of the shooter wheels (centimetres)
                # Calculate launch velocity (v)
                x = distance
                numerator = g * (x ** 2)
                denominator = 2 * (math.cos(theta) ** 2) * (x * math.tan(theta) - (height))
                v = math.sqrt(numerator / denominator)
                # Calculate angular velocity (omega)
                omega = v / r_wheel  # in rad/s
                # Convert to RPM
                rpm = (omega * 60) / (2 * math.pi)
                rpm = rpm * 1
                # Display results
                print(f"\nRequired Launch Velocity: {v:.2f} m/s")
                print(f"Required Angular Velocity: {omega:.2f} rad/s")
                print(f"Required RPM for Shooter Wheels: {rpm:.2f} RPM")


                print(f"Distance to basket: {distance:.2f} centimeters")
                # xcoord,ycoord=coordinate(distance,angle)

                xmin=x_center-(width/2)
                ymin=y_center-(height/2)
                xmax=x_center+(width/2)
                ymax=y_center+(height/2)

                confidence=round(box.conf[0].item(),3)
                frame=cv2.rectangle(frame,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(255,0,0),2)
                xoffset=x_center-320
                xoffset=round(xoffset,1)
                
                cv2.putText(frame,str(round(rpm)),(280,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                # cv2.putText(frame,str(ycoord),(340,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                cv2.putText(frame,str(distance),(500,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                cv2.putText(frame,str(xoffset),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
            
        cv2.imshow("distance",frame)
        if cv2.waitKey(1)==ord('q'):
            break
cap.release()
cap.destroyAllWindows()
