import csv
import sys
import math
import re
import json

def parseCSV(filename):
	'''
		read from CSV file, then process it in whatever way we want
	'''
	firstRow = True
	restaurant = dict()
	count = 0
	violationCode = dict()
	with open(filename, 'r') as csvfile:
		spamreader = csv.reader(csvfile.read().splitlines())
		for row in spamreader:
			# print row
			# Get rid of the first row which is titles
			if firstRow:
				# print row[22]
				# print row[23], row[24], row[25]
				firstRow = False
			else:
				if row[1] != '':
					if row[1] not in restaurant:
						count += 1
						restaurant[row[1]] = set()
					if row[2] != '':
						restaurant[row[1]].add(row[3])

						if row[2] not in violationCode:
							violationCode[row[2]] = row[3]

	print restaurant
	print count
	print violationCode
	
	return restaurant, violationCode

def writeCSV(data, fileName):
	'''
		Write into another csv file with the processed data
	'''

	with open('processed_' + fileName, 'w') as fp:
	    writer = csv.writer(fp, delimiter=',')
	    for restaurant in data:
	    	writer.writerow(list(data[restaurant]))

# To write dictionary into a file for debugging
def jsonWrite(data, fileName):
	with open(fileName, 'w') as outfile:
		json.dump(data, outfile, sort_keys = True, indent = 4)

def main():
	fileName = sys.argv[1]

	data = dict()
	violationCode = dict()

	data, violationCode = parseCSV(fileName)
	# print data

	writeCSV(data, fileName)



if __name__ == '__main__':
	main()