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
loop = 10



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


def toString(x):
  str = ''
  for i in x:
     str += i
  return str



#Main
print "Waiting for device"
device = MonkeyRunner.waitForConnection(5000,"emulator-5554")
print "Connected"

count = 0
while (count < loop):
	os.system("clear")
	print "Current test: ",count 
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
			device.touch(110,236, 'DOWN_AND_UP')

			MonkeyRunner.sleep(6)
			numb = numb + 2
		else:
			#2 If can't open app, sleeps
			print "Waiting for device"
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

	actionchoice = [' ', ' --pct-touch 1',' --pct-trackball 1',' --pct-nav 1',' --pct-majornav 1',' --pct-syskeys 1',' --pct-appswitch 1',' --pct-anyevent 1']

	exclude = filter( lambda x: random.randint(0,1) == 0, actionchoice)
 
	print "We are excludingL:", exclude
	os.system("adb -e shell monkey -p org.mozilla.fennec "+ toString(exclude) + " -v  500 ")


	

	#Logs actions and crashes
	#os.system("grep -A 5 -h -r CRASH REPORTS > REPORTS/Crashlogs/TestCrash"+`count`+".txt")

	# 4 Check rotate pos
	checkpos()

	# 6 Clears text
	print "Test: ", count," completed."
	MonkeyRunner.sleep(5)
	count = count + 1
		
	
	
	# 7 Restarts emulator
	print "Restarting..."
	device.shell('stop');
	MonkeyRunner.sleep(2)	
	device.shell('start');
	MonkeyRunner.sleep(5)
	numb = numb - 2
	
	
print "end"


