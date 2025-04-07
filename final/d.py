# from ultralytics import YOLO
import serial
import time
# import cv2
# from distance import calcdist,horizontal
import keyboard 
# from coords import coordinate
# from equation import calcrpm
# from errorfit import corrected_distance
# from polynomial_fit import predict_rpm
# model = YOLO(r'C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\best.pt')

try:
    ser = serial.Serial('COM3', 115200, timeout=1, rtscts=False, dsrdtr=False)
    print("Connected to teensy.")
    time.sleep(0.5)
except serial.SerialException as e:
    print(f"Failed to connect: {e}")
    exit()

# cap = cv2.VideoCapture(1)

while True:
    # ret, frame = cap.read()
    # if not ret:
    #     break
    

    # results = model.predict(source = frame,conf=0.25,save=True)
    # for i in results:
    #     for box in i.boxes:
    #         x_center, y_center, width, height = box.xywh[0].cpu().numpy()
    #         x_center, y_center, width, height = (
    #             float(x_center),
    #             float(y_center),
    #             float(width),
    #             float(height),
    #         )
        
            #confidence = float(box.conf[0].cpu().numpy())
            # class_id = int(box.cls[0].cpu().numpy())
            # class_name = results[0].names.get(class_id, "Unknown")
            
            # if class_name == "basket":
            #     # angle=0
            #     distance=calcdist(width)
            #     hori_dist=horizontal(distance)+1.5
            #     # print(f"Distance to basket: {distance:.2f} centimeters")
            #     # distance=corrected_distance(distance)
            #     # xcoord,ycoord=coordinate(distance,angle)
            #     rpm=predict_rpm(hori_dist/100) #def calcrpm(botheight,hoopheight,distance,angle,radius):
                


            #     xmin=x_center-(width/2)
            #     ymin=y_center-(height/2)
            #     xmax=x_center+(width/2)
            #     ymax=y_center+(height/2)

            #     confidence=round(box.conf[0].item(),3)
            #     frame=cv2.rectangle(frame,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(255,0,0),2)
            #     xoffset=x_center-320
            #     xoffset=round(xoffset,1)
                
            #     cv2.putText(frame,str(round(rpm)),(280,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
            #     # cv2.putText(frame,str(ycoord),(340,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
            #     cv2.putText(frame,str(distance),(500,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
            #     cv2.putText(frame,str(xoffset),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
    rpm=3600
    if keyboard.is_pressed('w') and rpm<4000:
        ser.write(str(int(round(rpm))).encode('utf-8'))
        print(f"Sent RPM: {int(round(rpm))}")
    # ser.flush()
    if keyboard.is_pressed('s'):
        x=0
        ser.write(str(int(round(x))).encode('utf-8'))
        print("Sent 0")

#         cv2.imshow("distance",frame)
#         if cv2.waitKey(1)==ord('q'):
#             break
# cap.release()
# cap.destroyAllWindows()
