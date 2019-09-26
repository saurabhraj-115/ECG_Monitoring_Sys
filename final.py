import serial
from os import system





ser = serial.Serial('/dev/ttyACM0', 9600)
while 1: 
	try:
		if(ser.in_waiting >0):
			line = ser.readline()
			cmd= "cd /home/pi/Desktop/aws-iot-device-sdk-python/samples/basicPubSub && sudo python basicPubSub.py -e a22m0pb0aki0bc-ats.iot.us-east-1.amazonaws.com -r root-CA.crt -c ECG_iot_RPi.cert.pem -k ECG_iot_RPi.private.key -t topic_1 -M "+ str(line)
			system(cmd)
	except KeyboardInterrupt:
		sys.exit()
