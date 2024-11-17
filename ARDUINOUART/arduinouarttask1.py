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
        ser.write(message.encode('utf-8'))
        ser.flush()
        data = ser.readline().decode('utf-8').strip()
        if data:
            print("Received from Arduino:",data)
        time.sleep(0.1)

finally:
    ser.close()
    print("Serial connection closed.")
