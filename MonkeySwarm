from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import commands
import sys
import random
import os
#Sets up $REPORTROOT
os.system("REPORTS=./reports")
os.system("rm REPORTS")
os.system("mkdir REPORTS")

# Number of repeats?
loop = 90



#Functions
def rotate():
  MonkeyRunner.sleep(2)
	os.system("/scratch/xautomation-1.07/xte \"keydown Control_L\"")
	os.system("/scratch/xautomation-1.07/xte \"keydown F12\"")
	MonkeyRunner.sleep(1)
	os.system("/scratch/xautomation-1.07/xte \"keyup Control_L\"")
	os.system("/scratch/xautomation-1.07/xte \"keyup F12\"")
	MonkeyRunner.sleep(10)


def sameAs(device, i1, i2, perc):
  e = ne = 0
  for x in range(0, int(device.getProperty('display.width'))):
    for y in range(0, int(device.getProperty('display.height'))):
      #print 'x = %d, y = %d ' % (x,y) 
      if i1.getRawPixelInt(x,y) == i2.getRawPixelInt(x,y):
        e = e+1
      else:
        ne = ne+1

  print 'e = %d, ne = %d' % (e,ne)
  match = e * 100.0 / (ne + e)
  if match >= perc:
    return True
  else:
    return False


def checkpos():
	check = device.takeSnapshot()	

#Checks if we are horizontal
	Horizontal = check.getSubImage((335,1200,50,70))
	checkHorizontal = MonkeyRunner.loadImageFromFile(path = './pics/horizontal2.png')
	if MonkeyImage.sameAs(Horizontal, checkHorizontal, 1.0):
		print "We are Horizontal"
		f = open("REPORTS/Rotation/Rotation"+`count`+".txt", "w")
		f.write("Position: Horizontal")
		f.close()

#Checks if we are vertical
	Vertical = check.getSubImage((340,1200,70,70))
	checkVertical = MonkeyRunner.loadImageFromFile(path = './pics/vertical1.png')
	if MonkeyImage.sameAs(Vertical, checkVertical, 1.0):
		print "We are Vertical"
		f = open("REPORTS/Rotation/Rotation"+`count`+".txt", "w")
		f.write("Position: Vertical")
		f.close()



#Main
print "Waiting for device"
device = MonkeyRunner.waitForConnection(5000,"emulator-5554")
print "Connected!"

count = 0
while (count < loop):


	# 1 Checks if device is operatable
	MonkeyRunner.sleep(4)

	numb = 0
	while numb < 1:

		check = device.takeSnapshot()
		icon = check.getSubImage((110,236,60,60))
		checkicon = MonkeyRunner.loadImageFromFile(path = './pics/icon.png')
		if MonkeyImage.sameAs(icon, checkicon, 0.5):
			# 2 Opens App
			print "Opening app"
			device.touch(100, 300, 'DOWN_AND_UP')
			MonkeyRunner.sleep(4)
			numb = numb + 2
		else:
			#2 If can't open app, sleeps
			print "Can't see app, sleeping"
			MonkeyRunner.sleep(5)
			numb = 0

	print "Test: ", count
		
	# 3 Rotate device or not	
	choice = ['sleep', 'rotate']
	rotateacc = random.choice(choice)
	
	if rotateacc == 'sleep':
		print "Not rotating"
		MonkeyRunner.sleep(1)

	if rotateacc == 'rotate':
		print "Rotating"
		rotate()

	

	


	# 5 Chooses action

	actionchoice = ['trackball','syskeys','normal']
	monkey = random.choice(actionchoice)
	
	if monkey == 'normal':
		print "Not excluding any actions"
		os.system("adb -e shell monkey -p org.mozilla.fennec -v  500 > REPORTS/Test"+`count`+".txt")
	
	if monkey == 'syskeys':
		print "Not using syskeys"
		os.system("adb -e shell monkey -p org.mozilla.fennec --pct-syskeys 1 -v  500 > REPORTS/Test"+`count`+".txt")
		
	if monkey == 'trackball':
		print "Not using trackball"
		os.system("adb -e shell monkey -p org.mozilla.fennec --pct-trackball 1 -v  500 > REPORTS/Test"+`count`+".txt")


	

	

	#Logs actions and crashes
	#os.system("grep -A 5 -h -r CRASH REPORTS > REPORTS/Crashlogs/TestCrash"+`count`+".txt")

	# 4 Check rotate pos
	checkpos()

	# 6 Clears text
	print "Clearing terminal txt"
	MonkeyRunner.sleep(5)
	count = count + 1
	os.system("clear")	
	
	
	# 7 Restarts emulator
	print "Stopping Emulator"
	device.shell('stop');
	MonkeyRunner.sleep(2)	
	print "Starting Emulator"
	device.shell('start');
	MonkeyRunner.sleep(5)
	numb = numb - 2

	
print "end"


