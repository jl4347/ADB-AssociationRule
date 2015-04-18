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
Query Modification Method
=================================================================================



=================================================================================
Addional effort to Query Modification Method
=================================================================================
