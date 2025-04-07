from ultralytics import YOLO
import cv2

model = YOLO(r'C:\Users\Happy Home\OneDrive\Desktop\ROBOCON\best.pt')
cap = cv2.VideoCapture(0)
h=[]
dia=[]
ground_y = None
def draw_horizontal_line(event, x, y, flags, param):
    global ground_y, frame
    if event == cv2.EVENT_LBUTTONDOWN:
        ground_y = y
        # Draw a horizontal line across the frame at the clicked y-coordinate
        cv2.line(frame, (0, ground_y), (frame.shape[1], ground_y), (0, 255, 0), 2)
        print(f"Line drawn at y-coordinate: {ground_y}")

cv2.namedWindow("distance")
cv2.setMouseCallback("distance", draw_horizontal_line)

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
            
            if class_name == "ball":
                xmin=x_center-(width/2)
                ymin=y_center-(height/2)
                xmax=x_center+(width/2)
                ymax=y_center+(height/2)
                h.append(y_center)
                dia.append(height)
                print(h)
                
                oldh=y_center
                confidence=round(box.conf[0].item(),3)
                frame=cv2.rectangle(frame,(int(xmin),int(ymin)),(int(xmax),int(ymax)),(255,0,0),2)
                ball_dia=23.5 #in cm
                if dia:
                    pixel_height=dia[h.index(min(h))]
                    unit_l=ball_dia/pixel_height
                if h and ground_y:
                    dist_ground_pixel=ground_y-min(h)
                    dist_ground=unit_l*dist_ground_pixel   #*1.15

                
                # xoffset=x_center-320
                # xoffset=round(xoffset,1)
                
                # cv2.putText(frame,str(round(rpm)),(280,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                # cv2.putText(frame,str(ycoord),(340,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
                # cv2.putText(frame,str(distance),(500,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
        
        if ground_y:
            cv2.line(frame, (0, ground_y), (frame.shape[1], ground_y), (0, 255, 0), 2)
        if h:
            cv2.line(frame, (0,int(min(h))),(frame.shape[1],int(min(h))), (255,0,0), 2)

        if ground_y and h:
            cv2.putText(frame,str(dist_ground),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)

        cv2.imshow("distance",frame)
        if cv2.waitKey(1)==ord('q'):
            break
cap.release()
cap.destroyAllWindows()
