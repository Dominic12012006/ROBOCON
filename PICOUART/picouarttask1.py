import serial
import time

try:
    ser = serial.Serial('COM3', 115200, rtscts=False, dsrdtr=False, timeout=1)
    print("Connected to Pico")
except serial.SerialException as e:
    print("Connection failed:", e)
    exit()

while True:
    
    message = input("Enter: ")
    message += "\n"
    ser.write(message.encode('utf-8'))  
    ser.flush() 

    time.sleep(0.1) 

    if ser.in_waiting:
        data = ser.readline().decode('utf-8').strip() 
        print("Received from Pico:", data)

ser.close()
