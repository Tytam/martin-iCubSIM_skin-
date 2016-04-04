import copy
import pprint
import time
import random
from examplereader import ExampleReader
from distancematrix import distancematrix
from left_arm_init import left_arm_init
import yarp;
yarp.Network.init();

class senso_motor_pair:
	def __init__(self):
		self.skin_cube_ID = None
		self.joints = [None] * 7
		return
	def __init__(self, ID, j):
		self.skin_cube_ID = ID.split()
		self.joints = copy.deepcopy(j);
		return
	
	def write(self):
		for item in self.skin_cube_ID:
			print item
		for x in range(0,6):
			print self.joints[x]
		return

	def writefile(self):
		for item in self.skin_cube_ID:
			vysledok  += str(item)
		for x in range(0,6):
			vysledok += ' '
			vysledok +=  str(self.joints[x])
		return vysledok
	
citac = ExampleReader()
#print citac.getData()

model = []

#prepare pasive hand
left = left_arm_init()
left.set()

###########################################################################
# prepare a property object
props = yarp.Property()
props.put("device","remote_controlboard")
props.put("local","/client/right_arm")
props.put("remote","/icubSim/right_arm")

# create remote driver
armDriver = yarp.PolyDriver(props)
#query motor control interfaces
iPos = armDriver.viewIPositionControl()
iEnc = armDriver.viewIEncoders()

#retrieve number of joints
jnts=iPos.getAxes()
print 'Controlling', jnts, 'joints'

# read encoders
encs=yarp.Vector(jnts)
iEnc.getEncoders(encs.data())
# store as home position
home=yarp.Vector(jnts, encs.data())

pprint.pprint(home.data())

#initialize a new tmp vector identical to encs
tmp=yarp.Vector(jnts)
for x in range(0, 4):
    print tmp.get(x)
# add 10 degrees to the first four joints
tmp.set(0, -30)
tmp.set(1, 10)
tmp.set(2, 40)
tmp.set(3, 50)
tmp.set(4, 0)
tmp.set(5, 0)
tmp.set(6, 0)
tmp.set(7, 59)
tmp.set(8, 20)
tmp.set(9, 20)
tmp.set(10, 145)
tmp.set(11, 10)
tmp.set(12, 10)
tmp.set(13, 58)
tmp.set(14, 154)
tmp.set(15, 167)

hom=yarp.Vector(jnts)
hom.set(1, 15)
hom.set(2, 40)
hom.set(3, 70)
hom.set(4, 20)
hom.set(5, 0)
hom.set(6, 0)
hom.set(7, 59)
hom.set(8, 20)
hom.set(9, 20)
hom.set(10, 20)
hom.set(11, 10)
hom.set(12, 10)
hom.set(13, 58)
hom.set(14, 154)
hom.set(15, 167)

# move to new position
iPos.positionMove(tmp.data())

tmp.set(1, 15)
tmp.set(2, 40)
tmp.set(3, 70)
tmp.set(4, 20)

iPos.positionMove(tmp.data())

print "posunute"

zname = [0,0,0,0,0,0,0,0,0,0,0]
joint_setting= [-30, 15, 40, 70, 20, 0, 0]
semafor = True
x = 0
while semafor:
	x += 1
	r = random.uniform(-92, -50)
	tmp.set(0, r)
	joint_setting[0] = r
	r = random.uniform(0, 28)
	tmp.set(1, r)
	joint_setting[1] = r
	r = random.uniform(50, 80)
	joint_setting[2] = r
	tmp.set(2, r)
	r = random.uniform(70, 105)
	joint_setting[3] = r
	tmp.set(3, r) 
	r = random.uniform(-90, 90)
	joint_setting[4] = r
	tmp.set(4, r)    
	r = random.uniform(-50, 0)
	joint_setting[5] = r
	tmp.set(5, r) 
	r = random.uniform(-19, 39)
	joint_setting[6] = r
	tmp.set(6, r) 
	iPos.positionMove(tmp.data())
	#print "zaspal"
	time.sleep(3)
	dat = citac.getData()
	print dat 
	if dat != "":
		model.append(senso_motor_pair(dat, joint_setting))
		d = dat.split()
		for item in d:
    			if item == "11":
				zname[0] = 1
			if item == "12":
				zname[1] = 1
			if item == "13":
				zname[2] = 1
			if item == "21":
				zname[3] = 1
			if item == "22":
				zname[4] = 1
			if item == "23":
				zname[5] = 1
			if item == "24":
				zname[6] = 1
			if item == "25":
				zname[7] = 1
			if item == "26":
				zname[8] = 1
			if item == "27":
				zname[9] = 1
			if item == "28":
				zname[10] = 1

		suma = 0
		for j in range(0, 10):
			suma += zname[j]
		if suma > 1:
			for k in range(0, 10)
				kamarati = getkamaratov(self, k, zname)
				if len(kamarati) > 1:
					semafor = False
				
	
	#print "zobudeny"
	iPos.positionMove(hom.data())
	time.sleep(2)
	print x



















################################################################################
f = open('workfile', 'w')
i = 0
while i < len(model):
	model[i].write()
	#f.write(model[i].writefile())
	#f.write('\n')	
	i += 1

i = 0
while i < len(model):
	f.write(model[i].writefile())
	f.write('\n')	
	i += 1

f.close()
	

	

