import csv
import sys

def parseCSV(filename):
	'''
		read from CSV file, then process it in whatever way we want
	'''
	firstRow = True
	data = list()
	with open(filename, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			if firstRow:
				firstRow = False
			else:
				data.append(row)
				# Manipulate the data to suit our needs
	
	return data

def main():
	fileName = sys.argv[1]

	data = list()

	data = parseCSV(fileName)
	# print data



if __name__ == '__main__':
	main()