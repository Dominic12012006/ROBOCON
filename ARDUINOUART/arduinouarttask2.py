import serial
import time

try:
    ser = serial.Serial('COM3', 9600, timeout=1, rtscts=False, dsrdtr=False)
    print("Connected to Arduino.")
    time.sleep(0.5)
except serial.SerialException as e:
    print(f"Failed to connect: {e}")
    exit()

try:
    while True:
        message = input("Enter: ")
        message += "\n"
        c=0
        for i in message:
            if i=='#':
                c+=1
        ser.write(message.encode('utf-8'))
        ser.flush()

        for j in range(0,c+1):
            data = ser.readline().decode('utf-8').strip() 
            print(j+1," : ", data)
        
        time.sleep(0.1)

finally:
    ser.close()
    print("Serial connection closed.")
