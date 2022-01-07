import sys
import time
start_time = time.time()

#testData = 3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3

#replicates once every 7 days

#fish on different schedules

#new fish takes 9 days to reproduce first time (2+) and does not reduce day count until day after berth

def fishLifeTracker(School, numDays):
	
	while numDays > 0: #using while loop reduces cost of 80 by 0.5s more than recursion. https://stackoverflow.com/questions/2651112/is-recursion-ever-faster-than-looping
		numDays -= 1
		newSchool=[]
		for fish in School:
			fish -=1

			if fish > -1:
				newSchool.append(fish)
			elif fish == -1:
				newSchool.append(6)
				newSchool.append(8)
				#newFish += 1
			else:
				print("invalid fish reproductive cycle number")
		#print(newSchool)
		School = newSchool
		
	return(School)

n = len(sys.argv)
#does not check if the arguments are valid assumes user input is as described
if n == 3:
	simDays = int(sys.argv[1])
	schoolDataFile = sys.argv[2]
	
	file = open(schoolDataFile, 'r')

	#would need catches for any unexpected data
	for line in file.readlines():
		fname = line.rstrip().split(',')

	schoolData = [int(item) for item in fname]

elif n == 1:
	simDays = 18
	schoolData = [3,4,3,1,2]
	print("SimDays: ", simDays)
	print("schoolData", schoolData)
else:
	print("fishSchool.py [Number of Days to Simulate] [Fish School Data File]\nEmpty runs simuation for 18 days with [3,4,3,1,2] dataset")

if n == 3 or n == 1: #clumsy way of doing this
	finalSchool = fishLifeTracker(schoolData, simDays)
	#print("Final School: ", finalSchool)
	print("Total Lanturn Fish:", len(finalSchool))
	print("--- %s seconds ---" % (time.time() - start_time))
