import time
import serial
import RPi.GPIO as GPIO

lock = 16
wheel = 18

GPIO.setmode(GPIO.BOARD)

GPIO.setup(lock,GPIO.OUT)
GPIO.setup(wheel,GPIO.OUT)

p = GPIO.PWM(lock,50)

r = GPIO.PWM(wheel,50)

def open_gate():
    p.start(2.5)
    p.ChangeDutyCycle(5)
    time.sleep(1)
    r.start(5)
    r.ChangeDutyCycle(1.5)
    time.sleep(2)
    r.ChangeDutyCycle(0)
    time.sleep(1)
    
def close_gate():
    p.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    r.start(5)
    r.ChangeDutyCycle(5)
    time.sleep(5)
    r.ChangeDutyCycle(0)
    time.sleep(0.5)
    
try:
    while True:
        print('Scan Your Card')
        PortRF = serial.Serial('/dev/serial0',9600)

        ID = ""
        read_byte = (PortRF.read())
        buf = read_byte.decode("utf-8")
        print(buf)
        for Counter in range(12):
            read_byte = (PortRF.read()).decode("utf-8")
            ID = ID + read_byte
            print (read_byte)
        print (ID)
        PortRF.close()
        if ID == '6100130F1964':
            print('Open')
            open_gate()
            
        else:
            print('Close')

except KeyboardInterrupt:
    print("Stopped")
finally:
    GPIO.cleanup()