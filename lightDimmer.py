from time import sleep
import RPi.GPIO as GPIO
delay = .1
inPin12 = 12
inPin40 = 40
outPin38 = 38
GPIO.setmode(GPIO.BOARD)
GPIO.setup(outPin38, GPIO.OUT)
GPIO.setup(inPin12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(inPin40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
myPWM = GPIO.PWM(outPin38, 100)

buttonStateDim = 1
buttonStateDimOld = 1
buttonStateBright = 1
buttonStateBrightOld = 1
brightness = 0
LEDstate = 0

def brighten():
    global LEDstate
    global brightness
    LEDstate = not LEDstate
    #buttonBrightPresses += 1
    if brightness < 90:
        brightness += 12.4
        myPWM.start(brightness)
    else:
        print("Bulb maxed")
    print(brightness)
    
def dim():
    global LEDstate
    global brightness
    LEDstate = not LEDstate
    #buttonBrightPresses -= 1
    if brightness > 10:
        brightness -= 12.4
        myPWM.start(brightness)
    else:
        print("Bulb off")
        
    print(brightness)
    

if __name__ == "__main__":
    
    try:
        
        while True:
            buttonStateDim = GPIO.input(inPin12)
            buttonStateBright = GPIO.input(inPin40)
            #print(buttonStateBright)
            if buttonStateBright == 0 and buttonStateBrightOld == 1 :
                brighten()

            
            if buttonStateDim == 0 and buttonStateDimOld == 1 :
                dim()
            
            buttonStateBrightOld = buttonStateBright
            buttonStateDimOld = buttonStateDim
            sleep(delay)
           

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("adios")

