import time
from os import system
import RPi.GPIO as GPIO
#import eeml
GPIO.setmode(GPIO.BOARD)
DEBLOGGER = 1
UG = 1


#i=1;
GPIO.setup(3, GPIO.IN)
while True:
		dat = GPIO.input(3)
		print dat
		#system("cd ~/Desktop/aws-iot-device-sdk-python/samples/basicPubSub")
		#cmd= "cd ~/Desktop/aws-iot-device-sdk-python/samples/basicPubSub && sudo python basicPubSub.py -e a22m0pb0aki0bc-ats.iot.us-east-1.amazonaws.com -r root-CA.crt -c ECG_iot_RPi.cert.pem -k ECG_iot_RPi.private.key -t topic_1 -M "+ str(dat)
		#system(cmd)	
	 
		




#while True:

      #if DEBUG:

            #if input:

                    #print('3.3')

           #else:

                    #print('0')

#time.sleep(1)
