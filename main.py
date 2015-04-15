import csv
import itertools
import sys

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
			row = [item for item in row if item != '' and item != ' ']
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

			if test_result:  
				Ck[tuple(test)] = 0
	print 'Ck:',Ck
	return Ck

def containsItem(record, itemset):
	'''
		This method check if a record contains a certain itemset
	'''
	for item in itemset:
		if item not in record:
			return False 
	return True


def apriori(data, lookup_base, min_supp):
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
		turn+=1
		print 'turn:', turn
		print 'Lk-1:',L[turn-1]
		print lookup
		C[turn] = generateCk(L[turn-1], lookup, turn)

		# traverse the data compute for Ck and lookup
		lookup = {}
		for record in data:
			for item in C[turn]:
				result = containsItem(record, item)
				if result:
					C[turn][item]+=1
					lookup.update({key:(lookup[key]+1 if lookup.has_key(key)
									else 1) for key in item })

		# compute for the Lk
		L[turn] = {key: C[turn][key] for key in C[turn].keys() 
					if C[turn][key] >= min_supp }
		print 'L[',turn,']', L[turn]
		print 

	print 'L: ',L

	return L


def getFreqSetAndRules(L,  min_conf, min_supp, total):
	'''
		This method take L as input, and output all rule with conf>min_conf
	'''
	print
	print '-----------getRules------------'
	rules = {}
	freqSet = {}

	# initialize freqSet
	if L.has_key(1): freqSet = {key:float(L[1][key])/total 
								for key in L[1].keys()}

	# compute for freqSet and rules
	for turn in range(2, len(L)):
		freqSet.update({key:float(L[turn][key])/total 
						for key in L[turn].keys()})

		# loop through each item in Lk
		for item in L[turn]:

			# get the LHS of each item
			last_itemset = itertools.combinations(item, turn-1)
			supp = float(L[turn][item])/total

			for aRule in last_itemset:
				conf = float(L[turn][item])/L[turn-1][aRule]
				if conf <min_conf:
					continue
				
				LHS = str(list(set(item)&set(aRule)))
				RHS = str(list(set(item)-set(aRule)))
				string = LHS + ' => '+ RHS \
					+ ' (Conf: '+str(conf)+', Supp: '+str(supp)+')'
				rules.update({string: conf})

	print freqSet
	print rules
	return freqSet, rules

def main():

	fileName = sys.argv[1]
	min_supp = float(sys.argv[2])
	min_conf = float(sys.argv[3])
	data, lookup = parseCSV(fileName)
	#print lookup
	# min_supp 0.3 min_conf 0.5

	total = len(data) 
	min_supp_num = len(data)*min_supp

	possible_rules = apriori(data, lookup, min_supp_num)
	freqSet, rules = getFreqSetAndRules(possible_rules, min_conf,\
						min_supp, total)
	output(freqSet, rules, min_supp, min_conf)

def output(freqSet, rules, min_supp, min_conf):
	import operator

	print
	print '-----------output--------------'
	
	freqSet_output = [str(list(key))+', '+str(value) for (key,value) 
				in sorted(freqSet.items(), key=operator.itemgetter(1))]

	freqSet_output.reverse()

	rules_output = [key for (key,value) in sorted(rules.items()
									, key=operator.itemgetter(1))]
	rules_output.reverse()

	with open('output.txt', 'w') as f:
		f.write("----Frequent itemsets (min_supp = "+ str(min_supp)+\
			")----\n\n")
		for item in freqSet_output:
			f.write(item+"\n")

		f.write("\n\n\n\n")
		f.write("----High-confidence association rules (min_conf = "+\
				str(min_conf)+")----\n\n")

		for item in rules_output:
			f.write(item+"\n")

if __name__ == '__main__':
	main()
