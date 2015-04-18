import csv
import sys
import math
import re

def parseCSV(filename):
	'''
		read from CSV file, then process it in whatever way we want
	'''
	firstRow = True
	data = list()
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
				if row[10] == 'Annual':
					# round annual salary to the nearest 10000
					row[8] = math.floor(int(row[8])/10000)*10000
					row[9] = math.ceil(int(row[9])/10000)*10000
				elif row[10] == 'Hourly':
					# round hourly salary to the nearest 5
					row[8] = math.floor(int(row[8])/5)*5
					row[9] = math.ceil(int(row[9])/5)*5

				# Posting Date only have month and year
				# row[22] = row[22][0:2] + row[22][6:9]
				# print row[22]
				
				# delete the Post until, Posting update and Process date dimension
				# print row[23], row[24], row[25]
				# del row[25]
				# del row[24]
				# del row[23]

				# delete the Recrument contact
				# del row[20]

				# combine the salary range from and range to fields
				# row.append(str(row[8]) + '-' + str(row[9]))
				row[8] = 'f' + str(int(row[8]))
				row[9] = 't' + str(int(row[9]))
				# print row[11]
				m = re.match("(\d+\/)\d+\/(\d+) \d+", str(row[11]))
				row.append(m.group(1) + m.group(2))
				del row[11]
				# del Num of position dimension
				del row[3]
				# del row[9]
				# del row[8]
				data.append(row)
	
	return data

def writeCSV(data, fileName):
	'''
		Write into another csv file with the processed data
	'''

	with open('processed_' + fileName, 'w') as fp:
	    writer = csv.writer(fp, delimiter=',')
	    writer.writerows(data)

def main():
	fileName = sys.argv[1]

	data = list()

	data = parseCSV(fileName)
	# print data

	writeCSV(data, fileName)



if __name__ == '__main__':
	main()