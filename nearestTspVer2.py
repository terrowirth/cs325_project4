# Nearing Neighbour Implementation of TSP
# Author: Tom Gariepy
# Last Updated: 3/7/2016
# Description: Nearest Neighbour implementation of TSP

#Imports
import math
import sys
import os # I don't think I need this
import time

def calcDistance(start, target):
	# x val
	x = abs(target[1] - start[1])

	# y val
	y = abs(target[2] - start[2])

	# triangle calc
	distance = round(math.sqrt((x**2) + (y**2)))

	#return result
	return distance



def minNext(start, unmarked, n):
	minDist = None
	minVal = None
	items = []

	# This is just to append distance where we are at so far into items, from start to n - 1
	for y in range(0, n - 1):
		selectVal = unmarked[y]
		selectDist = calcDistance(start, selectVal)
		item = []
		item.append(y)
		item.append(selectDist)
		items.append(item)

	# Does the actual calculation of and decision of what is minimum distance from n to end of graph
	for x in range(n, len(unmarked)):
		selectVal = unmarked[x]
		selectDist = calcDistance(start, selectVal)
		item = []
		item.append(x)
		item.append(selectDist)
		items.append(item)

		if (minDist == None):
			minDist = selectDist
			minVal = selectVal
		#elif(minVal < minDist):
		elif(selectDist < minDist):
			minDist = selectDist
			minVal = selectVal

	return minDist, minVal, items



def calcMin(start, graph):
	#unmarked = graph
	#unmarked.remove(start)
	path = []
	#items = []

	#path = [start]
	#path.append(start)
	currentV = start
	distance = 0

	#while (len(unmarked) > 0):
		#nextD, nextV = minNext(currentV, unmarked)
	#while (len(graph) > 0):
	for n in range(0, len(graph)):
		nextD, nextV, items = minNext(currentV, graph, n)

		distance = distance + nextD

		path.append(nextV)
		#unmarked.remove(nextV)

		currentV = graph[n]

	distance = distance + calcDistance(start, path[len(path) - 1])

	return distance, path, items



def calcPath(graph):
	minDist = None
	path = None
	curItems = []

	for x in range(0,len(graph)):
		resMin, resPath, items = calcMin(graph[x], graph)
		#graph = resPath
		
		if (minDist == None):
			minDist = resMin
			path = resPath
			curItems = items
		elif (resMin < minDist):
			minDist = resMin
			path = resPath
			curItems = items

	# With the path decided, sort the array from least distance to greatest
	curItems = sorted(curItems, key= lambda x: (x[1]))


	return minDist, curItems

def main():
	if (len(sys.argv) == 2):
		inName = sys.argv[1]
		outName = inName + ".tour"

		if (os.path.isfile(inName) == False):
			print("ERROR: " + inName + " not found.")
			return 1

		with open(outName, 'wt') as resultFile:

			with open(inName, 'rt') as inputFile:
				inData = inputFile.read().splitlines()

				for x in range(0, len(inData)):
					inData[x] = inData[x].split()

					inData[x][1] = int(inData[x][1])
					inData[x][2] = int(inData[x][2])

				tStart = time.time()
				minDist, path = calcPath(inData)
				tEnd = time.time()

				runTime = tEnd - tStart

				minDist = int(minDist)

				print("Time elapsed: ", runTime)
				print("Minimal Distance: ", minDist)

				resultFile.write(str(minDist) + "\n")

				for x in range(0,len(path)):
					resultFile.write(str(path[x][0]) + "\n")

		inputFile.close()
		resultFile.close()
	else:
		print("ERROR: Not enough variables!")

main()
# print("Running some code!")