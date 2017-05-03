import re

#from the sys package adding argv
from sys import argv

#  Read in the file here to a string named (exactly) text_contents
# Answer
script_name, input_file_path, out_file_path, search_term = argv
print input_file_path
print out_file_path
print search_term

input_file=open(input_file_path)
# print type (input_file_path)
# print type (out_file_path)

text_contents= input_file.read()
print text_contents

# These lines do the text search and print formatted results and a result
# count.



#  Change this line to take the search term from a command line parameter
 # search_term= raw_input("Search for: ")
 # search_results = re.findall("{50}" + search_term +"{50}", text_contents, re.DOTALL)
 # print "\n\n***\n\n ".join(search_results)
 # print len(search_results)


# Output the search results here to a file path from the commandline
