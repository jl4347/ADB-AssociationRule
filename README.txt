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

Then we used the "process.py" to further process the dataset. We basically make a 
dictionary to store all the description of the code that is violated by each
restaurant.

The goal of this dataset is to find the association rule of the violation codes.

=================================================================================
Internal design of our project
=================================================================================



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
