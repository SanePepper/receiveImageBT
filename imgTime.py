from PIL import Image
import serial
import time #from time import sleep
import winsound

bluetooth= serial.Serial('COM7',115200,timeout=1)
picSize = 120*184
camBuffer=b''
dataNum = 0
offset = 100
image = offset
receiveTime = time.process_time_ns()
data_time = time.process_time_ns()		
while image < offset+100 : 
	dataRead = bluetooth.inWaiting()
	if (dataRead > 0):
		if (time.process_time_ns() - receiveTime >= 1*1000*1000*1000):
			camBuffer = b''
			dataNum = 0
		camBuffer += bluetooth.read(dataRead)
		dataNum += dataRead
		receiveTime = time.process_time_ns()
		if (dataNum >= picSize):
			print(image)
			winsound.Beep(440, 300)
			img = Image.frombytes('L',(184,120),camBuffer)
			name = "img-"+str(image).zfill(3)+".bmp"
			img.save(name,"bmp")
			image = image+1
			camBuffer = b''
			dataNum = 0
print(time.process_time_ns()/1000/1000/1000)