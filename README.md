## `kmers.py`
`kmers.py` contains 2 utility functions for calculating Observed kmers and Possible kmers when a string and a positive integer are given.  
It also contains a utility function for calculating the linguistic complexity of a given string.  
### `count_kmers(text, k)`
`count_kmers(text, k)` calculates and returns the number of unique substrings of length k contained in the given string.  
### `possible_kmers(text, k)`
`possible_kmers(text, k)` calculates and returns the number of all possible kmers given the string.  
### `linguistic_complexity(text)`
`linguistic_complexity(text)` calculates a Pandas dataframe of comlumns `k`, `the number of observed kmers` and `the number of theoretically possible kmers for every k available` and outputs it to a `.csv` file.  
It returns the linguistic complexity of the given string.  
### `main(arg)`
`main(arg)` parses the command line interface, calls utility functions to calculate linguistic complexities of each lines given in an input file.  
## Running
`kmers.py` is run using the following format.  
```
python kmers.py -i <input file> -o <output file>
```
Input file should exist before calling this command.  
Output file is generated when it does not exist.  
## Testing
`test_kmers.py` thoroughly tests all utility functions defined in `kmers.py`.  
`kmers.py` is run using the following command.  
```
pytest -q test_kmers.py
```
`test_kmers.py` defines a class which contains 3 test cases for `linguistic_complexity(text)` and 5 test cases for `count_kmers(text, k)` and possible_kmers(text, k)