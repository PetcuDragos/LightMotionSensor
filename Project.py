import RPi.GPIO as GPIO
import time
import smbus

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER_ULTRA = 23   # trigger for ultrasensor
GPIO_ECHO_ULTRA = 24    # echo for ultrasensor
GPIO_LED = 26

GPIO.setup(GPIO_LED,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER_ULTRA, GPIO.OUT)
GPIO.setup(GPIO_ECHO_ULTRA, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_ULTRA, True)
    time.sleep(0.000000001)
    GPIO.output(GPIO_TRIGGER_ULTRA, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_ECHO_ULTRA) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_ECHO_ULTRA) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance

bus = smbus.SMBus(1)
DEVICE     = 0x23 # Default device I2C address
ONE_TIME_HIGH_RES_MODE_1 = 0x20

def convertToNumber(data):
     result=(data[1] + (256 * data[0])) / 1.2
     return (result)

def readLight(addr=DEVICE):
     # Read data from I2C interface
     data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
     return convertToNumber(data)

def light():
     lightLevel=readLight()
     level = float(format(lightLevel,'.2f'))
     return level


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            lig = light()
            print "Measurements are: distance = ", dist, ", light =", lig
            if dist< 10 and lig < 10 and dist > 1:
                GPIO.output(GPIO_LED,True)
            else:
                GPIO.output(GPIO_LED,False)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()

