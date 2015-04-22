Name: Mingfei Ge(mg3534), Jialun Liu(jl4347)

=================================================================================
How to run our program
=================================================================================

We have write a shell script to run the python program, just cd in the program
directory and do:

$ ./run.sh processed_Extract_DOHMH_New_York_City_Restaurant_Inspection_Results.csv 0.3 0.5
where 0.3 is the minimum support and 0.5 is the minimum confidence


=================================================================================
List of files we submit
=================================================================================
processed_Extract_DOHMH_New_York_City_Restaurant_Inspection_Results.csv

# code to process the data from NYC open group
process.py
# code to extract the association rule
main.py
run.sh

example-run.txt
README.txt

=================================================================================
Manipulation of the dataset from the NYC open group
=================================================================================
The dataset we used from the NYC open group is 
DOHMH_New_York_City_Restaurant_Inspection_Results.csv. This file is the inspection
results of the restaurants in the city of New York.

We first deleted some of the fields that we are not interested in. The dimensions
left are:
1. CAMIS
2. Restaurant name
3. Violation code
4. Violaton description

Then we used the "process.py" to further process the dataset. The idea of process 
is to make it similar to market basket. It group data by restaurant name, and make 
violation code of a restaurant in a single line or say a "basket". Then, we basically 
make a dictionary to store all the description of the code that is violated by each
restaurant.

The goal of this dataset is to find the association rule of the violation codes.

=================================================================================
Internal design of our project
=================================================================================
In this project, we implement original Apriori algorithm because we have built the 
integrated-dataset which is similar to that of market basket example (details already 
discussed above). The two main parts of this program are generating frequent itemset 
and filtering association rules. 

In terms of the first one, the high level idea is use the dynamic programming to build 
frequent itemset iteratively from the base itemset of size one until we can not generate 
any more frequent item whose support >= min_support . We maintain two dictionary Ck and 
Lk. Ck stands for the candidate item-set of size k, and Lk stands for frequent item-set 
of size k. Iteratively, we compute the candidate itemset 'Ck' based on itemset 'Ck-1', 
and test whether its subsets item-set 'Ck-1' of all combinations of size k-1 contained 
in the frequent itemset 'Lk'. Agrawal and Srikant paper's do it utilizing SQL self join 
query and removing wrongly insertions. To implement efficiently, we maintain a lookup 
list that contains all possible item in alphabet order in our program. The "testSubset" 
function actually does this work. We use python itertools to generate combinations of a 
candidate itemset, then test whether all these combinations in Lk-1. For example, if 
the Lk-1 contains {'diary, ink': 4, 'ink, pen':3} and the next word is 'pen', then we 
get the possible candidate item 'diary, ink, pen' and all combinations of size k-1 are 
['diary, ink', 'diary, pen', 'ink, pen']. The first 'diary, ink' must in the Lk because 
we get the 'diary, ink, pen' based on it. These other two gives us decision to append 
this to candidate item-set or not. In this example, we do not append since it does not 
have 'diary, pen'. By doing so, we could efficiently get the frequet item-set.

In addition, we have some small design to eliminate useless data and make it more 
efficient. We store the lookup things both in a list and in a dicitionary. In the 
dicitionary, the key is just the item itself and the value is the number of times Lk has 
this key. The reason is that if item appears in frequent item-set less than k-1 times, 
it cannot form a candidate item-set of size k. So we can ignore this data when computing 
candidate item-set of size k. For example, the data is like the following: 

A, B, C, D, E
   B, C, D
         D
A

The above data cannot have a frequent item-set of size 3 that contains item E, since E 
appears only once in the data set. 	 

Another part is to filtering out low confidence rules. The key idea is also a dynamic 
programming problem. We use Lk-1 to test for rules of Lk, where Lk is the same notation 
above. In each loop, we still compute the combination of k-1, and set them one by one 
to the left hand side and the rest of one item to the right hand side. We compute the 
Supp(left hand side)/ Supp(right hand side) and decide whether to filter out this rules. 
Because of the Apriori property that all subsets of frequent item-set is frequent, we 
could compute all these values.




=================================================================================
Discussion of the Association rules
=================================================================================
Results of the running the following command:
$ ./run.sh processed_Extract_DOHMH_New_York_City_Restaurant_Inspection_Results.csv 0.3 0.5


['Filth flies or food/refuse/sewage-associated (FRSA) flies present in facility\x1as food and/or non-food areas. Filth flies include house flies, little house flies, blow flies, bottle flies and flesh flies. Food/refuse/sewage-associated flies include fruit flies, drain flies and Phorid flies.'] => ['Cold food item held above 41\xe5\xbc F (smoked fish and reduced oxygen packaged foods above 38 \xe5\xbcF) except during necessary preparation.'] (Conf: 0.823170731707, Supp: 0.349792226839)

["Evidence of mice or live mice present in facility's food and/or non-food areas.", 'Non-food contact surface improperly constructed. Unacceptable material used. Non-food contact surface or equipment improperly maintained and/or not properly sealed, raised, spaced or movable to allow accessibility for cleaning on all sides, above and underneath the unit.'] => ['Cold food item held above 41\xe5\xbc F (smoked fish and reduced oxygen packaged foods above 38 \xe5\xbcF) except during necessary preparation.'] (Conf: 0.802627874237, Supp: 0.418088486923)

These rules suggest that there is a high chance that filth flies and mice are resulted from cold food being kept at temperature above 41F.


['Food not protected from potential source of contamination during storage, preparation, transportation, display or service.'] => ['Cold food item held above 41\xe5\xbc F (smoked fish and reduced oxygen packaged foods above 38 \xe5\xbcF) except during necessary preparation.'] (Conf: 0.794999172048, Supp: 0.46942067954)

This rule suggests that keeping food under 41F is the proper way to protec the food from the potential source of contamination.


['Plumbing not properly installed or maintained; anti-siphonage or backflow prevention device not provided where required; equipment or floor not properly drained; sewage disposal system in disrepair or not functioning properly.', 'Cold food item held above 41\xe5\xbc F (smoked fish and reduced oxygen packaged foods above 38 \xe5\xbcF) except during necessary preparation.'] => ['Food not protected from potential source of contamination during storage, preparation, transportation, display or service.'] (Conf: 0.74357661992, Supp: 0.355120997311)

The rule above suggests that the main potential source of contaminations are:
1. Plumbing not properly installed or maintained;
2. Cold food item held above 41F


["Evidence of mice or live mice present in facility's food and/or non-food areas."] => ['Hot food item not held at or above 140\xe5\xbc F.'] (Conf: 0.587044534413, Supp: 0.32608164263)

Similar to the cold food rule, it suggests that hot food not kept above 140F could the main cause of mice presence as well.


In general, this mining of association rule is helpful as it can indeed help the restaurants to identify the main cause of the code violation, for example:
1. cold food kept under 41F
2. hot food kept above 140F
3. plumming
4. seal the food properly

Identifying these sources could help the restaurant to focus on the main issue that cause food contaimination, filth flies, mice presence etc. Therefore could help the
restaurant to focus on the main cause and improve the inspection score and grade without wasting their effort on the superficial aspects.


=================================================================================
Addional effort to Query Modification Method
=================================================================================
