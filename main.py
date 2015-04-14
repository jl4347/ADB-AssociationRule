import csv
import collections
import itertools

def parseCSV(filename):
	'''
		read from CSV file, then sort and return the data
	'''
	data = []
	lookup_base = {}
	with open(filename, 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			row.sort()
			data.append(row)
			lookup_base.update( { item: (lookup_base[item]+1
								if lookup_base.has_key(item)
								else 1 ) 
								for item in row} )	
	return data, lookup_base


def testSubset(testset ,testlist, size):
	'''
		This method takes a testlist with size k and testset as input,
		the output is True if possible combinations with size of k-1
		in testset, otherwise False
		
	'''
	subset = itertools.combinations(testlist, size)
	for elem in subset:
		print 'elem:', elem
		if elem not in testset: return False
	return True


def generateCk(Lk_1, lookup, times):
	'''
		This method takes list form of Lk-1 and lookup as input 
		and output Ck.
		The procedure is first generate combinations of k-size itemset,
		then check for the all subset with k-1 size. 

		The lookup table is a list contains all possible tokens, the 
		format is like {'pen':4, 'ink':3, 'diary':3, 'soap':2}
	'''

	# Lk_1={('diary','pen'):3, ('ink', 'pen'): 3 , ('diary','ink'):2}
	# times = 3
	# lookup = {'pen':4, 'ink':3, 'diary':3, 'soap':2}
	last_itemset = [item for item in Lk_1.keys()]
	last_itemset.sort()
	# delete those tokens that can never be a combination because num is 
	# smaller than times-1. eg: turn 3 make item size of 3. If a token
	# appears less than 2 times, it can not form a conbination
	tokens = [item for item in lookup.keys() if lookup[item]>=times-1]
	tokens.sort()
	
	Ck = {}
	for item in last_itemset:
		print 'item:',item
		# delete already used tokens thus work on small num of tokens
		delword = item[-1]
		if delword in tokens: del tokens[0:tokens.index(delword)+1]
		
		print 'tokens left:', tokens
		if tokens == []: break

		# iterate through tokens list 
		for token in tokens:
			test = list(item)
			test.append(token)
			print 'the possible item to be test:',test
			test_result = testSubset(last_itemset, test, times-1)
			print test_result

			if test_result:  
				Ck[tuple(test)] = 0
	print 'Ck:',Ck
	return Ck

def containsItem(record, )


def apriori(data, lookup_base, min_supp, min_conf):
	'''
		Implement apriori algorithm:

		The Lk is a dic where k is the times of iteration (k), and value 
		is a also dic that stores <item, count> pairs.
		A list associated with Lk contains the keys in order.

		The format for Lk is like: {k-1:{...}, k: { (b,c,d):33, (a,b,c):40}}
		The format for the list is [(a,b,c), (b,c,d)]

		The Ck is similar to Lk, except for more  <item, count> pairs.
	'''
	L = {}
	C = {}

	# initialize C1 and L1
	C[1] = {tuple([key]):lookup_base[key] for key in lookup_base.keys()}
	L[1] = {tuple([key]):lookup_base[key] for key in lookup_base.keys() 
			if lookup_base[key]>= min_supp }
	#print 'L1',L[1]

	turn = 1
	lookup = lookup_base
	while L.has_key(turn) and L[turn]!={}:
		print L[turn], turn
		turn+=1
		C[turn] = generateCk(L[turn-1], lookup, turn)

		# traverse the data compute for L and lookup
		#for record in data:
	return L


	

def getRules(L):
	'''
		This method take L as input, and output all rule with conf > min_conf
	'''
	


def main():
	data, lookup = parseCSV('test.csv')
	print lookup
	# min_supp 0.3 min_conf 0.5

	min_supp = len(data)*0.7
	min_conf = len(data)*0.8
	apriori(data, lookup, min_supp, min_conf)

	


if __name__ == '__main__':
	main()
