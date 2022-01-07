import sys
import time
import numpy as np
from multiprocessing.pool import ThreadPool as Pool
start_time = time.time()

pool_size = 4  # your "parallelness"

#testData = 3,4,1,1,5,1,3,1,1,3,5,1,1,5,3,2,4,2,2,2,1,1,1,1,5,1,1,1,1,1,3,1,1,5,4,1,1,1,4,1,1,1,1,2,3,2,5,1,5,1,2,1,1,1,4,1,1,1,1,3,1,1,3,1,1,1,1,1,1,2,3,4,2,1,3,1,1,2,1,1,2,1,5,2,1,1,1,1,1,1,4,1,1,1,1,5,1,4,1,1,1,3,3,1,3,1,3,1,4,1,1,1,1,1,4,5,1,1,3,2,2,5,5,4,3,1,2,1,1,1,4,1,3,4,1,1,1,1,2,1,1,3,2,1,1,1,1,1,4,1,1,1,4,4,5,2,1,1,1,1,1,2,4,2,1,1,1,2,1,1,2,1,5,1,5,2,5,5,1,1,3,1,4,1,1,1,1,1,1,1,4,1,1,4,1,1,1,1,1,2,1,2,1,1,1,5,1,1,3,5,1,1,5,5,3,5,3,4,1,1,1,3,1,1,3,1,1,1,1,1,1,5,1,3,1,5,1,1,4,1,3,1,1,1,2,1,1,1,2,1,5,1,1,1,1,4,1,3,2,3,4,1,3,5,3,4,1,4,4,4,1,3,2,4,1,4,1,1,2,1,3,1,5,5,1,5,1,1,1,5,2,1,2,3,1,4,3,3,4,3

#replicates once every 7 days

#fish on different schedules

#new fish takes 9 days to reproduce first time (2+) and does not reduce day count until day after berth

# def schoolThread(School):
# 	newSchool=[]
# 	for fish in School:
# 		fish -=1

# 		#[newSchool.append(fish) if fish > -1 else (newSchool.extend(newFish))] #slower, extend takes more time and I am not sure how to add in a single statement

# 		if fish > -1:
# 			newSchool.append(fish)
# 		elif fish == -1:
# 			newSchool += newFish
# 		else:
# 			print("invalid fish reproductive cycle number")
# 	#print(newSchool)
# 	return newSchool

def fishLifeTracker(School, numDays):
	newFish=[6,8]

	while numDays > 0: #using while loop reduces cost of 80 by 0.5s more than recursion. https://stackoverflow.com/questions/2651112/is-recursion-ever-faster-than-looping
		numDays -= 1
		newSchool=[]
		for fish in School:
			fish -=1 #had logic attached to this to begin with, but realized it just counts down to -1

			#[newSchool.append(fish) if fish > -1 else (newSchool.extend(newFish))] #slower, extend takes more time and I am not sure how to add in a single statement

			if fish > -1:
				newSchool.append(fish)
			elif fish == -1:
				newSchool += newFish
			else:
				print("invalid fish reproductive cycle number")

		#print(newSchool)
		School = newSchool #tried to just overwrite school as I went to save writes, but it ended up slower as it becomes more individual writes

		##multiprocessing try
		##can't parallelize due to each array being dependent on the last.. Does find the next day multiple times really fast! :)
		# pool = Pool(pool_size)
		# School = [pool.apply(schoolThread, args=(School,)) for x in range(1,numDays)]

		# while numDays > 0: #using while loop reduces cost of 80days by ~0.5s more than recursion. https://stackoverflow.com/questions/2651112/is-recursion-ever-faster-than-looping
		# 	numDays -= 1
		# 	newSchool=[]
		# 	newFish = [6,8]

		# #numpy try
		# #for this try I manipulated the array as a whole 
		# import numpy as np
		# School = [fish - 1 for fish in np.array(School)] #subtract 1 from entire array
		# count = np.count_nonzero(np.array(School) == -1) #long part here, count the values that are -1
		# School = np.append(np.array(School), count*[6,8])#then reset reproductive cycle and create new fish
		# #School = np.delete(np.array(School), -1)#slower deletion of -1s
		# School = School[(School>-1)] #get rid of all negative ones
		# #numpy try

	#clippedSchool = School[(School>-1)] #try removing all negatives at the end, but it added cost due to the array size increasing.
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

